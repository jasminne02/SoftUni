from django.urls import path, include

from OnlineLibrary.web import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add book'),
    path('edit/<int:pk>/', views.edit_book, name='edit book'),
    path('details/<int:pk>/', views.details_book, name='book details'),
    path('delete/<int:pk>/', views.delete_book, name='book delete'),
    path('profile/', include([
        path('', views.profile_details, name='profile'),
        path('edit', views.profile_edit, name='edit profile'),
        path('delete', views.profile_delete, name='delete profile'),
    ])),
]
