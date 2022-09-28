from django.urls import path, include
from Petstragram.pets import views


urlpatterns = [
    path('add/', views.add, name='add'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', views.show_pet_details, name='pet-details'),
        path('edit/', views.edit, name='pet-edit'),
        path('delete/', views.delete, name='pet-delete'),
    ])),
]
