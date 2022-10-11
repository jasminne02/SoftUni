from django.shortcuts import render

from Petstragram.pets.models import Pet


def add(request):
    return render(request, 'pets/pet-add-page.html')


def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.objects.all()
    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def delete(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
