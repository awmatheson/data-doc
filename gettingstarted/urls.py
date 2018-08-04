from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views



urlpatterns = [

    url(r'^signup/$', hello.views.signup, name='signup'),
    url(r'^account_activation_sent/$', hello.views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<repository>.*)/(?P<dag_name>.*)$',hello.views.activate, name='activate'),
    url(r'^user/(?P<username>.*)/edit/$', hello.views.edit_profile, name="edit_profile"),
    url(r'^user/(?P<username>.*)$', hello.views.view_profile, name="view_profile"),
    url(r'^password/$', hello.views.change_password, name='change_password'),
    url(r'^add_database/$', hello.views.add_database, name='add_database'),
    url(r'^delete_database/(?P<db_alias>.*)/(?P<id>[\d]+)/$', hello.views.delete_database, name='delete_database'),
    url(r'^$', hello.views.index, name='index'),
    url(r'^info', hello.views.info, name='info'),
    url(r'^TOC/(?P<repo_id>.*)/DAG/(?P<dag_name>.*)/task/(?P<job_name>.*)/table/(?P<table_name>.*)$', hello.views.table, name="table"),
    url(r'^TOC/(?P<repo_id>.*)/DAG/(?P<dag_name>.*)/task/(?P<job_name>.*)$', hello.views.task, name='task'),
    url(r'^TOC/(?P<repo_id>.*)/DAG/(?P<dag_name>.*)$', hello.views.DAG, name='DAG'),
    url(r'^TOC/(?P<repo_id>.*)$', hello.views.TOC, name='TOC'),
    path('admin/', admin.site.urls),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]