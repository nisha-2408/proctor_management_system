from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.homepage, name="home"),
    path('student/signin/',views.student_signin , name='student_signin'),
    path('student/signup/', views.student_signup , name='student_signup'),
    path('signout', views.signout , name='signout'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path("forgotPassword", views.forgotPassword,name="forgotPassword"),
    path('resetPassword/<uidb64>/<token>',views.resetPassword,name="resetPassword"),
    path("resetPassword/done/",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done",),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="authentication/password/password_reset_complete.html"),name="password_reset_complete",),
    path("faculty/signin", views.faculty_signin, name="faculty_signin"),
    path("faculty/signup", views.faculty_signup, name="faculty_signup"),
    path('dashboard', views.dashboard, name="dashboard")
]
