from django.shortcuts import render

from .models import CountryData, TownData
from .forms import CountryForm


def index(request):
    data = CountryData.objects.all()
    data2 = TownData.objects.all()
    form = CountryForm()

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'data': data,
        'data2': data2,
        'form': form,
    }

    return render(request, 'index.html', context)

