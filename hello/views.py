from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password

from .forms import *
from .models import *
from .tokens import account_activation_token
from scripts.customcode import *

# Create your views here.

# Create Account Page 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your data-doc account.'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'repository': form.cleaned_data.get('repository'),
                'dag_name': form.cleaned_data.get('dag_directory_name'),
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
    	form = SignUpForm()

    args = {'form':form}
    return render(request, 'signup.html', args)


# Link from email to activate account
def activate(request, uidb64, token, repository, dag_name):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True
		user.profile.repository = repository
		user.profile.dag_directory_name = dag_name
		user.save()
		user.profile.save()
		login(request, user)

		user.profile.first_name = user.first_name
		user.profile.last_name = user.last_name
		user.profile.email = user.email
		user.profile.save()
		return redirect('index')
	else:
		return render(request, 'account_activation_invalid.html')


# Shows page to confirm account activation email has been sent
def account_activation_sent(request):
	return render(request, 'account_activation_sent.html')


# Change Password
@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	args = {'form':form}
	return render(request, 'change_password.html', args)

# Shows user profile
@login_required
def view_profile(request, username):

	return render(request, 'userProfile.html')

# Changes to user profile
@login_required
def edit_profile(request, username):

	if request.method == 'POST':
		confirm_password_form = ConfirmPasswordForm(request.POST, instance=request.user)
		form = EditProfileForm(request.POST, instance=request.user.profile)

		if form.is_valid() and confirm_password_form.is_valid():
			profile = form.save(commit=False)
			current_user = request.user
			current_user.first_name = profile.first_name
			current_user.last_name = profile.last_name
			current_user.email = profile.email
			current_user.save()
			profile.user = request.user
			profile.save()

			return redirect('view_profile', request.user.username)

	else:
		current_profile = request.user.profile
		form = EditProfileForm(instance=current_profile)
		confirm_password_form = ConfirmPasswordForm()
	args = {'form':form, 'confirm_password_form':confirm_password_form}
	return render(request, 'changeProfile.html', args)


# Shows form to add a database connection
@login_required
def add_database(request):

	if request.method == 'POST':
		a = Database()
		form = DatabaseForm(request.POST, instance=a)
		if form.is_valid():
			database = form.save(commit=False)
			database.user = request.user
			database.save()
			current_repository = request.user.profile.repository
			return redirect('TOC', current_repository)

	else:
		form = DatabaseForm()

	args = {'form':form, }
	return render(request, 'add_database.html', args)

@login_required
def delete_database(request, db_alias, id):

	db = Database.objects.get(pk=id)

	if request.method == 'POST':
		confirm_password_form = ConfirmPasswordForm(request.POST, instance=request.user)

		if confirm_password_form.is_valid():
			Database.objects.get(pk=id).delete()
			current_repository = request.user.profile.repository
			return redirect('TOC', current_repository)

	else:
		confirm_password_form = ConfirmPasswordForm()

	args = {'db':db, 'confirm_password_form':confirm_password_form}
	return render(request, 'delete_database.html', args)


# Index/Home Page (shows Search Function)
@login_required
def index(request):
	test = 'test'
	return render(request, 'index.html')


# Information/"How it works" page
def info(request):
	return render(request, 'info.html')


# Table of Contents/List of DAGS (results of Search Function)
@login_required
def TOC(request, repo_id):

	# Use variable repo_id to find DAGS in repo
	DAG_list = get_repo()
	current_user = request.user
	DB_list = Database.objects.filter(user = current_user)

	args = {'DB_list':DB_list, 'repo_id': repo_id, 'DAG_list': DAG_list}
	return render(request, 'TOC.html', args)


# One page per DAG included in repo, shows list of tasks/jobs in DAG
@login_required
def DAG(request, repo_id, dag_name):

	# Use variables repo_id and dag_name to find SQL jobs
	SQL_list = get_DAG()
	args = {'repo_id': repo_id,
			'dag_name': dag_name,
			'SQL_list': SQL_list
	}
	return render(request, 'DAGS.html', args)


# One page per job/task, shows tables used within task and link to task file
@login_required
def task(request, repo_id, dag_name, job_name):

	# Use variables repo_id, dag_name and job_name to find tables
	TBL_list = get_job()
	args = {'repo_id': repo_id,
			'dag_name': dag_name,
			'job_name': job_name,
			'TBL_list': TBL_list
	}
	return render(request, 'task.html', args)


# One page per table, shows columns and data types
@login_required
def table(request, repo_id, dag_name, job_name, table_name):

	TBL_connection_list = get_tables()
	args = {'repo_id': repo_id,
			'dag_name': dag_name,
			'job_name': job_name,
			'table_name': table_name,
			'TBL_connection_list': TBL_connection_list
	}
	return render(request, 'table.html', args)