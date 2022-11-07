from django.urls import path

from .views import SignUpView, register

urlpatterns = [
    path("signup/", register, name="signup"),
]
