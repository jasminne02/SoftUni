from django import http
from django.shortcuts import render
from django101.tasks.models import Task


# Shows task template
def index(request):
    context = {
        'title': 'The tasks app',
    }

    return render(request, 'index.html', context)


# Shows all tasks ordered by id
def show_all_tasks(request):
    all_tasks = Task.objects \
        .order_by('id') \
        .all()

    context = {
        'title': 'All tasks:',
        'tasks': all_tasks
    }

    return render(request, 'index_all.html', context)


# Shows 'It Works!' template
def show_bare_minimum_view(request):
    contex = {
        'title': 'It Works!'
    }

    return render(request, 'index_it_works.html', contex)
