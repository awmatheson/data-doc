from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#from .models import Greeting

from scripts.customcode import *

# Create your views here.


# Index/Home Page (shows Search Function)
def index(request):

    return render(request, 'index.html')


# Information/"How it works" page
def info(request):

	return render(request, 'info.html')


# Table of Contents/List of DAGS (results of Search Function)
def TOC(request):

	# Retrieve URL from search form
	if request.method == 'GET':
		repo_id = request.GET.get('repo_id', None)

	# Use variable repo_id to find DAGS in repo
	DAG_list = get_repo()

	return render(request, 'TOC.html', {'repo_id': repo_id, 'DAG_list': DAG_list})


# One page per DAG included in repo, shows list of tasks/jobs in DAG
def DAG(request, repo_id, dag_name):

	# Use variables repo_id and dag_name to find SQL jobs
	SQL_list = get_DAG()

	return render(request, 'DAGS.html', {'repo_id': repo_id, 'dag_name': dag_name, 'SQL_list': SQL_list})


# One page per job/task, shows tables used within task and link to task file
def task(request, repo_id, dag_name, job_name):

	# Use variables repo_id, dag_name and job_name to find tables
	TBL_list = get_job()

	return render(request, 'task.html', {'repo_id': repo_id, 'dag_name': dag_name, 'job_name': job_name, 'TBL_list': TBL_list})


# One page per table, shows columns and data types
def table(request, repo_id, dag_name, job_name, table_name):

	TBL_connection_list = get_tables()

	return render(request, 'table.html', {'repo_id': repo_id, 'dag_name': dag_name, 'job_name': job_name, 'table_name': table_name, 'TBL_connection_list': TBL_connection_list})



# --Built in view from 'Getting Started'
# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, 'db.html', {'greetings': greetings})

# --Not using this view anymore
# def repo(request):
# 	if request.method == 'GET':
# 		repo_id = request.GET.get('repo_id', None)
# 	return render(request, 'TOC.html', {'repo_id': repo_id})