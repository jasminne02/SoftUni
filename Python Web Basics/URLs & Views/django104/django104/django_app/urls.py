from django.urls import path
from django104.django_app import views

urlpatterns = [
    path('', views.index),
    path('moreinfo/<int:id>/', views.more_info),
    path('moreinfo/<int:id>/return', views.return_index),
]
