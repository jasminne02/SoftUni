from django.urls import path, include
from MyMusicApp.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', include([
        path('details/<int:pk>/', views.details_album, name='details album'),
        path('add/', views.add_album, name='add album'),
        path('edit/<int:pk>/', views.edit_album, name='edit album'),
        path('delete/<int:pk>/', views.delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('add/', views.add_profile, name='add profile'),
        path('details/', views.details_profile, name='details profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ])),
]
