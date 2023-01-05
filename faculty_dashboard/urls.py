from django.urls import path,include
from . import views

app_name = 'faculty'

urlpatterns = [
    path('/dashboard/', views.dashboard, name="dashboard"),
]