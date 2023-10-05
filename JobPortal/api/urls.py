from django.urls import path
from . import views

urlpatterns=[
    path('',views.GetRoutes),
    path('users',views.getUsers)
]