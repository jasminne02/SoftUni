from django.urls import path

from ClassBasedViews.web import views


urlpatterns = [
    path('', views.IndexViewWithTemplate.as_view()),
    path('create/', views.EmployeeCreateView.as_view(), name='employee create')
]
