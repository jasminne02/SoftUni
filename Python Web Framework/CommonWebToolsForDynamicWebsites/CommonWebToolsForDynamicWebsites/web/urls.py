from django.urls import path

from CommonWebToolsForDynamicWebsites.web import views


urlpatterns = [
    path('', views.index),
    path('sessions/', views.session_view),
]
