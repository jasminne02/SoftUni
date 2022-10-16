from django.contrib import admin
from django.urls import path, re_path

from .views import home_page, about_page, contacts_page, example_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('contacts/', contacts_page),
    path('about/', about_page),
    path('example/', example_page),
    re_path(r'^pages?/$', about_page)
]
