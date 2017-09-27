"""Routes for managing user account manipulation."""

from django.conf.urls import url
from .views import NewUser, EditUser, RemoveUser, PostMessage


urlpatterns = [
    url(r'^new/', NewUser.as_view(), name='new'),
    url(r'^edit/$', EditUser.as_view(), name='edit_page'),
    url(r'^edit/(?P<pk>[0-9]+)/$',  EditUser.as_view(), name='admin_edit_page'),
    url(r'^remove/(?P<pk>[0-9]+)/$',  RemoveUser.as_view(), name='remove_user'),
    url(r'^show/(?P<pk>[0-9]+)/$',  PostMessage.as_view(), name='post_message'),
]