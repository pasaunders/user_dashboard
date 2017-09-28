"""Routes for managing user creation and editing and registration."""

from django.conf.urls import url
from .views import user_list
# , edit_page, add_page, add, edit, admin, admin_edit_page


urlpatterns = [
    url(r'^$', user_list.as_view(template_name='dashboard_manager/index.html'), name='user_home'),
    url(r'^admin$', user_list.as_view(template_name='dashboard_manager/index.html'), name='admin_home'),
]