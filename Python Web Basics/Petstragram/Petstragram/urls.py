from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Petstragram.common.urls')),
    path('accounts/', include('Petstragram.accounts.urls')),
    path('pets/', include('Petstragram.pets.urls')),
    path('photos/', include('Petstragram.photos.urls')),
]
