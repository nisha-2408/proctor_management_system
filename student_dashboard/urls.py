from django.urls import path,include
from . import views

app_name = 'student'

urlpatterns = [
    path('/dashboard/<str:pk>/', views.dashboard, name="dashboard"),
    path('/marks/<str:pk>/', views.dashboard_marks, name="marks"),
    path('/courses/register/', views.registerCourses, name='register'),
    path('/courses/edit/', views.editCourseDetails, name='edit'),
    path('/courses/update/', views.updateCourseDetails, name='update'),
]
