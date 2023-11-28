from django.urls import path
from . import views

urlpatterns=[
    # path('',views.GetRoutes),
    path('login/', views.check_login),
    path('profiles',views.getProfiles),
    path('profiles/<str:username>/', views.getProfile),
    path('getid/<str:username>/', views.getId),
    path('jobposts/',views.getJobPosts),
    path('jobposts/<str:pk>/',views.getJobPost),
    path('jobapplications/',views.getJobApplications),
    path('jobapplications/<str:id>/',views.getJobApplication),
    path('waitlist/<str:jobid>/<str:username>/',views.getWaitlist)

]