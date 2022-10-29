from django.urls import path, include

from GamesPlay.web import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('game/', include([
        path('create/', views.game_create, name='game create'),
        path('details/<int:pk>/', views.game_details, name='game details'),
        path('edit/<int:pk>/', views.game_edit, name='game edit'),
        path('delete/<int:pk>/', views.game_delete, name='game delete'),
    ])),
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('details/', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ])),
]
