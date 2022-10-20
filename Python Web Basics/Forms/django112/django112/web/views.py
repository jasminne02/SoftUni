from django.shortcuts import render

from django112.web.forms import PersonForm
from django112.web.models import Person


def index(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
        Person.objects.create(
            name=name,
        )

    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'index.html', context)
