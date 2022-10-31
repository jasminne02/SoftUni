from django.urls import path, include

from CarCollectionApp.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('car/', include([
        path('create/', views.car_create, name='car create'),
        path('<int:car_id>/details/', views.car_details, name='car details'),
        path('<int:car_id>/edit/', views.car_edit, name='car edit'),
        path('<int:car_id>/delete', views.car_delete, name='car delete'),
    ])),
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('details/', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ])),
]
