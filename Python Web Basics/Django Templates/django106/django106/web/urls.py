from django.urls import path
from django106.web import views


urlpatterns = [
    path('', views.index, name='index'),

