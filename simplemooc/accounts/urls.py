from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url, include
from simplemooc.accounts import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^entrar/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
	url(r'^sair/$', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
	url(r'^cadastre-se/$', views.register, name='register'),
	#url(r'^(?P<pk>\d+)/$', details, name='details'),
]
