from django.urls import path
from UserAndPasswordManagement.web.views import home_view, register_view, CustomLoginView, UserRegistrationView, \
    CustomLogoutView

from django.contrib.auth import views

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
