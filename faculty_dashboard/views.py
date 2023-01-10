from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student_dashboard.models import Student, StudentDetail, Sem, Fastrack

# Create your views here.
@login_required
def dashboard(request):
    faculty = Faculty.objects.get(email=request.user.email)
    students = Student.objects.filter(proctor_id=faculty)
    context = {'faculty': faculty, 'students': students}
    return render(request, 'faculty_dashboard/dashboard.html', context)

def studentDetails(request, pk):
    s_info = StudentDetail.objects.get(USN=pk)
    student = Student.objects.get(USN=pk)
    courses = Sem.objects.filter(sem=student.current_sem, USN=pk)
    fastrack = Fastrack.objects.filter(USN=pk, is_active=True)
    length = fastrack.count()
    context = {'s_info': s_info, 'courses': courses, 'fasttrack': fastrack, 'fast_count': length, 'email': student.email}
    return render(request, 'faculty_dashboard/student_details.html', context)

def approve(request, pk):
    s_info = StudentDetail.objects.get(USN=pk)
    s_info.isApproved = True;
    s_info.save()
    return redirect('faculty:student-details', pk=pk)