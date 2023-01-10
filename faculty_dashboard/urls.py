from django.urls import path,include
from . import views

app_name = 'faculty'

urlpatterns = [
    path('/dashboard/', views.dashboard, name="dashboard"),
    path('/student/<str:pk>', views.studentDetails, name="student-details"),
    path('/student/approved/<str:pk>', views.approve, name="student-details-approve")
]