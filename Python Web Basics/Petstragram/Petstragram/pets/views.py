from django.shortcuts import render


def add(request):
    return render(request, 'pets/pet-add-page.html')


def show_pet_details(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')


def edit(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def delete(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
