from django.shortcuts import render


def add(request):
    return render(request, 'photos/photo-add-page.html')


def show_photo_details(request, pk):
    return render(request, 'photos/photo-details-page.html')


def edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
