from django.urls import path
from django112.web import views


urlpatterns = [
    path('', views.index, name='index'),
]
