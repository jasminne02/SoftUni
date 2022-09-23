from django.urls import path
from django103.departments.views import show_department, show_department_details


urlpatterns = (
    # /departments/
    path('', show_department),

    # /departments/{department_id}/
    path('<department_id>/', show_department),

    # /departments/int/{department_id}/
    path('int/<int:department_id>/', show_department_details),
)
