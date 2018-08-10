from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .models import Profile, Database

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, required=True, help_text='Required.')
	repository = forms.CharField(max_length=300, required=True, help_text='Required. Enter Github Repository URL.')
	dag_directory_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter Dag Directory Name.')

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'repository',
			'dag_directory_name',
			'password1',
			'password2'
		)

class EditProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = (
			'first_name',
			'last_name',
			'email',
			'repository',
			'dag_directory_name'
		)

class ConfirmPasswordForm(forms.ModelForm):
	confirm_password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('confirm_password',)

	def clean(self):
		cleaned_data = super(ConfirmPasswordForm, self).clean()
		confirm_password = cleaned_data.get('confirm_password')
		if not check_password(confirm_password, self.instance.password):
			self.add_error('confirm_password', 'Password does not match.')

	def save(self, commit=True):
		user = super(ConfirmPasswordForm, self).save(commit)
		if commit:
			user.save()
			return user

	def get_object(self):
		return self.request.user

class DatabaseForm(forms.ModelForm):

	class Meta:
		model = Database
		fields = (
			'db_alias',
			'db_type',
			'db_connection_url'
		)