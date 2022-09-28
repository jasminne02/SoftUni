import random

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}; Age: {self.age}'


def index(request):
    context = {
        'title': 'Hello there!',
        'values': list(range(20)),
        'student': Student('Doncho', 19),
        'student_info': Student('Doncho', 19).get_info(),
        'students': [],
    }
    return render(request, 'index.html', context)


def show_some_page(request):
    return render(request, 'some_page.html')


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')
