from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Greeting
from .models import Repo
from .forms import RepoForm

from scripts.customcode import test
from scripts.customcode import test2

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
	if request.method == 'POST':
		form = RepoForm(request.POST)
		if form.is_valid():
			repo_url = form.save()
			#repo_url = Repo.__str__
			#repo_url.save()
			#repo_url = Repo.repo_url
			return render(request,'repo.html', {'repo_url': repo_url})
		else:
			return HttpResponseRedirect('/')
	else:
		form = RepoForm()

	#x = test()
	return render(request, 'repo.html', {'repo_url': repo_url})

def TOC(request):
	#r = Repo.repo_url
	x = test('[URL]')
	y = test2()
	DAG_list = ['one','two','three','four']
	return render(request, 'TOC.html', {'y': y, 'x': x, 'DAG_list': DAG_list})


