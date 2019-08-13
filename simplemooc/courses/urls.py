from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from simplemooc.courses import views
from simplemooc.courses.views import index, details
urlpatterns = [ 
	url(r'^$', index, name='index'),
	url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
	#url(r'^(?P<pk>\d+)/$', details, name='details'),
]
