from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Greeting
from .models import Repo
from .forms import RepoForm

from scripts.customcode import *

# Create your views here.
def index(request):

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def DAG(request, name):

	return render(request, 'DAGS.html', {'name': name})

def info(request):

	return render(request, 'info.html')

def repo(request):
	if request.method == 'GET':
		repo_id = request.GET.get('repo_id', None)
	# 	form = RepoForm(request.POST)
	# 	print(request)
	# 	if form.is_valid():

	# 		repo_url = form.save()
	# 		return render(request,'repo.html', {'repo_id': repo_id})
		
	# 	else:
	# 		return HttpResponseRedirect('/')
	# else:
	# 	form = RepoForm()

	return render(request, 'TOC.html', {'repo_id': repo_id})

def TOC(request):
	if request.method == 'GET':
		repo_id = request.GET.get('repo_id', None)

	DAG_list = get_repo()

	x = test('[URL]')
	y = test2()
	#DAG_list = ['one','two','three','four']
	return render(request, 'TOC.html', {'repo_id': repo_id, 'y': y, 'x': x, 'DAG_list': DAG_list})


