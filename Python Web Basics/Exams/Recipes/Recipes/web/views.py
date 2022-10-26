from django.shortcuts import render, redirect

from Recipes.web.models import Recipe
from Recipes.web.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = RecipeEditForm(instance=recipe)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    context = {
        'recipe': recipe,
    }

    return render(request, 'details.html', context)
