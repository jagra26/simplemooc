from django.conf.urls import include, url
from simplemooc.forum import views
from simplemooc.forum.views import forumIndex
urlpatterns = [
    url(r'^$', forumIndex, name='forumIndex'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', forumIndex, name='forumIndex_tagged'),
]