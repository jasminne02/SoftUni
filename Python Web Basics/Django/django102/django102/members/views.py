from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django102.members.models import Members


def index(request):
    all_members = Members.objects.all().values()
    context = {
        'members': all_members
    }
    return render(request, 'myfirst.html', context)


def add(request):
    return render(request, 'add.html')


def add_record(request):
    first_name = request.POST['first']
    last_name = request.POST['last']
    member = Members(firstname=first_name, lastname=last_name)
    member.save()
    return HttpResponseRedirect(reverse(index))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse(index))


def update(request, id):
    member = Members.objects.get(id=id)
    context = {
        'member': member,
    }
    return render(request, 'update.html', context)


def update_record(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse(index))


def template(request):
    return render(request, 'templates.html')
