from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.models import User


class user_list(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(user_list, self).get_context_data(**kwargs)
        if 'delete_user' in [x[3] for x in self.request.user.user_permissions.values_list()]:
            context['permission'] = 'admin'
        return context