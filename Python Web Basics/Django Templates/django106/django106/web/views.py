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
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Doncho', 19),
        'student_info': Student('Doncho', 19).get_info(),
        'students': [],
    }

    return render(request, 'index.html', context)
