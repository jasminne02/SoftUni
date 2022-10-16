from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return render(request, "hello_world.html", {"title": rendered_string})


def contacts_page(request):
    return render(request, "hello_world.html", {"title": "Contact us"})


def about_page(request):
    return render(request, "hello_world.html", {"title": "About us"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
