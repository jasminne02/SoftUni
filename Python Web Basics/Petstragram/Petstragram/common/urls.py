from django.urls import path
from Petstragram.common import views


urlpatterns = [
    path('', views.show_homepage, name='homepage'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id/', views.copy_link_to_clipboard, name='share')
]
