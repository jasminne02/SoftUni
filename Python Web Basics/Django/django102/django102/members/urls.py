from django.urls import path
from django102.members import views


urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('add/addrecord/', views.add_record),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('update/updaterecord/<int:id>', views.update_record),
]
