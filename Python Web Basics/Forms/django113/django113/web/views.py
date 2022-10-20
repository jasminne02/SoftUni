from django.http import HttpResponse
from django.shortcuts import render
from django113.web import forms


def index(request):
    if request.method == 'GET':
        form = forms.ToDoForms()
    else:
        form = forms.ToDoForms(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


def images(request):
    if request.method == 'GET':
        form = forms.ImageForm()
    else:
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()
            return render(request, 'show-img.html', {'images': images})

    context = {
        'form': form,
    }
    return render(request, 'images.html', context)
