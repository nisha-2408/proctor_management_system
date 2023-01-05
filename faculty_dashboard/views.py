from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student_dashboard.models import Student

# Create your views here.
@login_required
def dashboard(request):
    faculty = Faculty.objects.get(email=request.user.email)
    students = Student.objects.filter(proctor_id=faculty)
    context = {'faculty': faculty, 'students': students}
    return render(request, 'faculty_dashboard/dashboard.html', context)