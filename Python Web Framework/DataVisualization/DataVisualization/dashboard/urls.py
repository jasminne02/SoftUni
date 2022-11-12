from django.urls import path

from DataVisualization.dashboard import views


urlpatterns = [
    path('', views.index, name='dashboard'),
]
