from django.urls import path, include
from FitnessWebsite.accounts import views


urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.show_profile_details, name='profile-details'),
        path('edit/', views.show_profile_edit, name='profile-edit'),
        path('delete/', views.show_profile_delete, name='profile-delete'),
    ]))
]
