from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from Petstragram.common.models import Like
from Petstragram.photos.models import Photo


def show_homepage(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
