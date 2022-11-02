import random
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render
from ClassBasedViews.web import models


class IndexView(views.View):
    def get(self, request):
        return HttpResponse('It works from CBV')

    def post(self, request):
        pass

    # In Django Rest Framework
    # def put(self, request):
    #     pass


class IndexViewWithListView(views.ListView):
    context_object_name = 'employees'
    model = models.Employee
    template_name = 'index.html'
    extra_context = {'title': 'List View'}  # static context

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name=pattern.lower())

        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template View'}  # static context

    # dynamic context
    def get_content_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = models.Employee.objects.all()
        return context


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    model = models.Employee
    fields = '__all__'


class ExampleView:
    def __init__(self):
        self.value = random.randint(1, 15)

    @classmethod
    def get_view(cls):
        return cls().view

    def view(self, request):
        return HttpResponse(f'It works! {self.value}')
