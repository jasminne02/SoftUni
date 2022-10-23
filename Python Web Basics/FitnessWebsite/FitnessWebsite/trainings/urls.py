from django.urls import path
from FitnessWebsite.trainings import views


urlpatterns = [
    path('', views.show_trainings, name='classes'),
]
