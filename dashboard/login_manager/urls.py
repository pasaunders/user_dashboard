"""Routes for managing user login and registration."""

from django.conf.urls import url
from .views import (
    index, signin_page, register_page, register, login_user
    )


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^signin$', signin_page, name='signin_page'),
    url(r'^register$', register_page, name='register_page'),
    url(r'^add_user$', register, name='register'),
    url(r'^login$', login_user, name='login'),
]