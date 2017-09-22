"""Routes for managing user login and registration."""

from django.conf.urls import url
from .views import index, signin, register


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^signin$', signin, name='signin'),
    url(r'^register$', register, name='register'),
]