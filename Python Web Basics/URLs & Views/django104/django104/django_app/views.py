from django.shortcuts import render, reverse, redirect
from django104.django_app import models
from django.http import HttpResponseRedirect


def index(request):
    all_members = models.People.objects.all()
    context = {
        'members': all_members
    }
    return render(request, 'index.html', context)


def more_info(request, id):
    member = models.People.objects.get(id=id)
    context = {
        'member': member
    }
    return render(request, 'moreinfo.html', context)


def return_index(request, id):
    return redirect(index)
