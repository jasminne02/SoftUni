from django.shortcuts import render, redirect

from django111.web.models import Employees


def index(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'index.html', context)

