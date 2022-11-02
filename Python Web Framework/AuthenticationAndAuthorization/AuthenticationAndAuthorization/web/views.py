from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User


def index(request):
    new_user = User.objects.create_user(
        username='jasmine',
        password='password',
    )
    user_message = '' if request.user.is_authenticated else ' not '
    return HttpResponse(f'The user is {user_message} authenticated')


def create_user_and_login(request):
    user = User.objects.create_user(
        username='Name',
        password='User.objects.create_',
    )

    login(request, user)


def permission_debug(request):
    usernames = {'jasmine'}
    users = User.objects.filter(username__in=usernames)
    return HttpResponse('It works')
