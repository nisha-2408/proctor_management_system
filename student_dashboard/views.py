from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from student_dashboard.models import Student, courseRequest

# Create your views here.
@login_required
def dashboard(request, pk):
    student=Student.objects.get(email=request.user.email)
    if(pk!=student.USN):
        return HttpResponse("Not allowd")
    courses = models.Sem.objects.filter(USN=pk)
    print(courses)
    context = {'courses': courses}
    return render(request, 'student_dashboard/courses_registered.html', context)

@login_required
def registerCourses(request):
    student=Student.objects.get(email=request.user.email)
    numbers=courseRequest.objects.get(student_usn=student.USN)
    no=[]
    o=numbers.no_subjects
    while o>0:
        no.append(o)
        o-=1
    print(no, o)
    context = {'usn': student.USN, 'number': no}
    return render(request, 'student_dashboard/course_register_form.html', context)
