from django.shortcuts import render


def show_homepage(request):
    return render(request, 'common/home-page.html')
