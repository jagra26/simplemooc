from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from simplemooc.forum import views

urlpatterns = [ 
	url(r'^$', index, name='index'),
]