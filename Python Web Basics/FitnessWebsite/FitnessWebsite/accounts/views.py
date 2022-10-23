from django.shortcuts import render


def log_in(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def show_profile_details(request, pk):
    return render(request, 'accounts/profile_details.html')


def show_profile_edit(request, pk):
    return render(request, 'accounts/profile_edit.html')


def show_profile_delete(request, pk):
    return render(request, 'accounts/profile_delete.html')

