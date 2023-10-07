from django.urls import path
from . import views

urlpatterns=[
    path('',views.GetRoutes),
    path('students',views.getStudents),
    path('managers',views.getManagers),
    path('departments',views.getDepartments)
]