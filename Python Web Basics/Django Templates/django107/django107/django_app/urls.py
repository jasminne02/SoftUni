from django.urls import path
from django107.django_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('some-page/', views.show_some_page, name='some-page'),
    path('some-page/go-to-homepage/', views.redirect_to_home, name='redirect to home'),
    path('about/', views.about, name='about'),
]
