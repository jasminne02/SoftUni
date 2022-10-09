from django.urls import path
from django111.web import views


urlpatterns = [
    path('', views.index),
]
