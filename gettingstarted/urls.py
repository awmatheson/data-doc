from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('TOC/DAG/<str:name>/', hello.views.DAG, name='DAG'),
    url(r'^info', hello.views.info, name='info'),
    url(r'^repo/', hello.views.repo, name='repo'),
    path('TOC/', hello.views.TOC, name='TOC'),
    path('admin/', admin.site.urls),
]
