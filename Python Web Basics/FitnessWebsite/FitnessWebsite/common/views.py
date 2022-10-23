from django.shortcuts import render


def show_homepage(request):
    return render(request, template_name='common/home-page.html')
