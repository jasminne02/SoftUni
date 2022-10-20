from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django113.web import views


urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.images, name='images'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
