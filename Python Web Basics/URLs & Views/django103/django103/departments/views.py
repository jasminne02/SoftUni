from django.http import HttpResponse
from django.shortcuts import render


def show_department(request, *args, **kwargs):
    body = f'path:{request.path}  args={args}, kwargs={kwargs}'
    return HttpResponse(body)


def show_department_details(request, department_id):
    body = f'path:{request.path};  id: {department_id}'
    return HttpResponse(body)
