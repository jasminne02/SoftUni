from django.shortcuts import render, redirect

from NotesApp.web.models import Profile, Note
from NotesApp.web.forms import ProfileCreateForm, NoteCreateForm, NoteEditForm, NoteDeleteForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'notes': Note.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'core/home-no-profile.html', context)


def profile_details(request):
    notes_count = Note.objects.count()
    profile = get_profile()

    context = {
        'notes_count': notes_count,
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


def profile_delete(request, pk):
    profile = Profile.objects.filter(pk=pk).get()
    profile.delete()
    notes = Note.objects.all()
    notes.delete()
    return redirect('index')


def add(request):
    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'notes/note-create.html', context)


def edit(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'notes/note-edit.html', context)


def delete(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note
    }

    return render(request, 'notes/note-delete.html', context)


def details(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {
        'note': note,
    }
    return render(request, 'notes/note-details.html', context)
