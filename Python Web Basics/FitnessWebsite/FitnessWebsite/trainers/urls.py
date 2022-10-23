from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from FitnessWebsite.trainers import views


urlpatterns = [
    path('', views.show_trainers, name='trainers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
