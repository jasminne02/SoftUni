from django.urls import path, include

from NotesApp.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add note'),
    path('edit/<int:pk>/', views.edit, name='edit note'),
    path('delete/<int:pk>/', views.delete, name='delete note'),
    path('details/<int:pk>/', views.details, name='note details'),
    path('profile/', include([
        path('', views.profile_details, name='profile'),
        path('delete/<int:pk>', views.profile_delete, name='profile delete'),
    ])),
]
