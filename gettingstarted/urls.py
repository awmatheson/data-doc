from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # Un-used URLs----
    #url(r'^db', hello.views.db, name='db'),
    #path('repo/', hello.views.repo, name='repo'),


    url(r'^$', hello.views.index, name='index'),
    url(r'^info', hello.views.info, name='info'),
    url(r'^TOC/(?P<repo_id>.*)/DAG/(?P<dag_name>.*)/task/(?P<job_name>.*)/table/(?P<table_name>.*)$', hello.views.table, name="table"),
    url(r'^TOC/(?P<repo_id>.*)/DAG/(?P<dag_name>.*)/task/(?P<job_name>.*)$', hello.views.task, name='task'),
    url(r'^TOC/(?P<repo_id>.*)/DAG/(?P<dag_name>.*)$', hello.views.DAG, name='DAG'),
    url(r'^TOC/?$', hello.views.TOC, name='TOC'),
    path('admin/', admin.site.urls),
]