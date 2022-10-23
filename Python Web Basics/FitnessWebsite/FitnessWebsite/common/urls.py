from django.urls import path
from FitnessWebsite.common import views


urlpatterns = [
    path('', views.show_homepage, name='home'),
]
