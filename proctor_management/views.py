from django.shortcuts import render, redirect

def homepage(request):
    return render(request, "index.html")

def faculty_sigin(request):
    return render(request, "faculty_signin.html")

def student_sigin(request):
    return render(request, "student_signin.html")

def password_reset_done(request):
    return render(request, "password_reset_done.html")