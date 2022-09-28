from django.urls import path, include
from Petstragram.photos import views


urlpatterns = [
    path('add/', views.add, name='add'),
    path('<int:pk>/', include([
        path('', views.show_photo_details, name='photo-details'),
        path('edit/', views.edit, name='photo-edit'),
    ])),
]
