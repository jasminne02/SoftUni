from django.shortcuts import render

from Petstragram.photos.models import Photo


def add(request):
    return render(request, 'photos/photo-add-page.html')


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
    return render(request, 'photos/photo-edit-page.html')
