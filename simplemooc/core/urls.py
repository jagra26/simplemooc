from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from simplemooc.core import views
from simplemooc.core.views import home, contact
urlpatterns = [
	url(r'^$', home, name = 'home'),
    url(r'^contato/$', contact, name = 'contact'),
]