from django.shortcuts import render

from FitnessWebsite.trainers.models import Trainer


def show_trainers(request):
    all_trainers = Trainer.objects.all()
    context = {
        'all_trainers': all_trainers,
    }

    return render(request, 'trainers/trainers.html', context)

