from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FitnessWebsite.common.urls')),
    path('about/', include('FitnessWebsite.about.urls')),
    path('accounts/', include('FitnessWebsite.accounts.urls')),
    path('trainers/', include('FitnessWebsite.trainers.urls')),
    path('trainings/', include('FitnessWebsite.trainings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
