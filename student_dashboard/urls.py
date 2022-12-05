from django.urls import path,include
from . import views

app_name = 'student'

urlpatterns = [
    path('/dashboard/<str:pk>/', views.dashboard, name="dashboard")
]
