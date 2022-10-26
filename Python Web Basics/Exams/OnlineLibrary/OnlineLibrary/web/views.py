from django.shortcuts import render, redirect

from OnlineLibrary.web.models import Profile, Book
from OnlineLibrary.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, BookAddForm, BookEditForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def home(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'profile': profile,
        'books': Book.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


def add_book(request):
    if request.method == 'GET':
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'books/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'book': book,
        'profile': get_profile(),
    }
    return render(request, 'books/edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'profile': get_profile()
    }
    return render(request, 'books/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'core/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()
            books = Book.objects.all()
            books.delete()
            return redirect('home')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profiles/delete-profile.html', context)
