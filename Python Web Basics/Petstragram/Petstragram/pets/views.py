from django.shortcuts import render, redirect

from Petstragram.pets.models import Pet
from Petstragram.pets.forms import PetForm, PetDeleteForm


def add(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context)


def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.objects.all()
    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {'form': form}
    return render(request, 'pets/pet-edit-page.html', context)


def delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}

    return render(request, 'pets/pet-delete-page.html', context)
