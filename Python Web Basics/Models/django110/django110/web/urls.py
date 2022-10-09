from django.urls import path
from django110.web import views


urlpatterns = [
    path('', views.home),
]
