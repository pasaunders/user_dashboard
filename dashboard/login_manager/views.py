"""Manage information between login/register pages and the ORM."""


from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import signin_form, register_form
from .models import Profile


def index(request):
    return render(request, 'login_manager/index.html')


def signin_page(request):
    context = {
        'signin_form': signin_form
    }
    return render(request, 'login_manager/signin.html', context)


def register_page(request):
    context = {
        'register_form': register_form
    }
    return render(request, 'login_manager/register.html', context)


def register(request):
    """Register a user to the built in model."""
    if request.method == 'POST':
        errors = Profile.objects.user_validator(request.POST)
        # if errors:
        #     for tag, error in errors.items():
        #         messages.error(request, error, extra_tags=tag)
        #     return redirect(reverse('login:register_page'))
        # else:
        User.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            )
        if len(User.objects.all()) is 1:
            User.objects.first().user_permissions.add(
                Permission.objects.get(codename='admin')
                )
    return redirect(reverse('login:home'))


def login_user(request):
    """Login existing user."""
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['email'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('invalid password')
    return redirect(reverse('login:home'))
