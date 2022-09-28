from django.urls import path
from Petstragram.common import views


urlpatterns = [
    path('', views.show_homepage, name='homepage'),
]
