from django.urls import path
from FitnessWebsite.about import views


urlpatterns = [
    path('', views.show_about_page, name='about'),
]
