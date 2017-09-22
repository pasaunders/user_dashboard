"""Manage information between login/register pages and the ORM."""


from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from bcrypt import hashpw, checkpw
from .forms import signin_form, register_form


def index(request):
    return render(request, 'login_manager/index.html')


def signin(request):
    return render(request, 'login_manager/signin.html')


def register(request):
    return render(request, 'login_manager/register.html')
