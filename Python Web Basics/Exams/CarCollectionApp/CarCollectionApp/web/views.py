from django.shortcuts import render, redirect

from CarCollectionApp.web.models import Profile, Car
from CarCollectionApp.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_total_car_price():
    cars = Car.objects.all()
    total_price = 0

    for car in cars:
        total_price += car.price

    return total_price


def index(request):
    context = {
        'hide_nav_links': True if not get_profile() else False,
    }

    return render(request, 'core/index.html', context)


def catalogue(request):
    context = {
        'cars': Car.objects.all(),
        'cars_count': Car.objects.count(),
    }
    return render(request, 'core/catalogue.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'cars/car-create.html', context)


def car_details(request, car_id):
    car = Car.objects.get(pk=car_id)

    context = {
        'car': car,
    }

    return render(request, 'cars/car-details.html', context)


def car_edit(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'cars/car-edit.html', context)


def car_delete(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        form.save()
        return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'cars/car-delete.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'hide_nav_links': True if not get_profile() else False,
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)


def profile_details(request):

    context = {
        'profile': get_profile(),
        'total_car_price': get_total_car_price,
    }

    return render(request, 'profiles/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)
