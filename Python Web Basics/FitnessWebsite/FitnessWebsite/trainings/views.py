from django.shortcuts import render

from FitnessWebsite.trainings.models import Training, TrainingType


def show_trainings(request):
    all_trainings = Training.objects.all()
    all_training_types = TrainingType.objects.all()

    context = {
        'all_trainings': all_trainings,
        'all_training_types': all_training_types,
    }

    return render(request, 'trainings/trainings.html', context)

