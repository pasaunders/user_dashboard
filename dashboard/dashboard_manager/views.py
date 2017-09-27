from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.models import User


class user_list(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(NewUser, self).get_context_data(**kwargs)
        if any(d['codename'] == 'admin' for d in self.request.user.user_permissions.values()):
            context['permission'] = 'admin'
        return context