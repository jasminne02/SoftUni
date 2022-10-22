from django.shortcuts import render, redirect

from Petstragram.photos.models import Photo
from Petstragram.photos.forms import PhotoCreateForm


def add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'photos/photo-add-page.html', context)


def show_photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit(request, pk):
    photo = Photo.objects.get(pk)
    if request.method == 'GET':
        form = PhotoCreateForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoCreateForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo-details')

    return render(request, 'photos/photo-edit-page.html')


def delete(request, pk):
    photo = Photo.objects.get(pk)
    photo.delete()
    return redirect('home')
