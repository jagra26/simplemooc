from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from simplemooc.courses import views
from simplemooc.courses.views import index, details, enrollment, announcements, undo_enrollment
urlpatterns = [ 
	url(r'^$', index, name='index'),
	url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
	url(r'^(?P<slug>[\w_-]+)/inscricao/$', enrollment, name='enrollment'),
	url(r'^(?P<slug>[\w_-]+)/anuncios/$', announcements, name='announcements'),
	url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', undo_enrollment, name='undo_enrollment'),
]
