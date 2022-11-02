from django.urls import path

from AuthenticationAndAuthorization.web import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user_and_login, name='login'),
    path('permissions/', views.permission_debug, name='permissions'),
]
