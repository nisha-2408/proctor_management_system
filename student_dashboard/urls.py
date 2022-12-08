from django.urls import path,include
from . import views

app_name = 'student'

urlpatterns = [
    path('/dashboard/<str:pk>/', views.dashboard, name="dashboard"),
    path('/courses/register/', views.registerCourses, name='register'),
    path('/courses/edit/', views.editCourseDetails, name='edit')
]
