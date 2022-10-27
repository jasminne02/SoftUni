from django.urls import path, include

from ExpensesTracker.web import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_expense, name='create expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete expense'),
    path('profile/', include([
        path('', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ])),
]
