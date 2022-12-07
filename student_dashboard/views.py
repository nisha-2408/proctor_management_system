from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from student_dashboard.models import Student, courseRequest, Sem

# Create your views here.
@login_required
def dashboard(request, pk):
    student=Student.objects.get(email=request.user.email)
    number=courseRequest.objects.filter(student_usn=student.USN)
    sem=student.current_sem
    if(pk!=student.USN):
        return HttpResponse("Not allowd")
    courses = models.Sem.objects.filter(USN=pk, sem=sem)
    print(courses)
    context = {'courses': courses, 'req': number.count(), 'sem': sem, 'var': 0}
    return render(request, 'student_dashboard/courses_registered.html', context)

@login_required
def registerCourses(request):
    o=0
    student=Student.objects.get(email=request.user.email)
    if courseRequest.objects.count() > 0:
        if courseRequest.objects.exists():
            number=courseRequest.objects.filter(student_usn=student.USN)
            if number.count() >0:
                numbers=number.get(student_usn=student.USN)
                sem=numbers.sem
                o=numbers.no_subjects
    no=[]
    if request.method=="POST":
        while o>0:
            ccode=request.POST['code%s' %(o)]
            cname=request.POST['name%s' %(o)]
            credit=request.POST['credits%s' %(o)]
            registration=request.POST['reg%s' %(o)]
            attempt=request.POST['attempt%s' %(o)]
            semob = Sem(USN=student.USN, sem=sem, courseName=cname, courseCode=ccode, credit=credit, registration=registration, attemptNumber=attempt)
            semob.save()
            o-=1
        numbers.delete()
        return HttpResponse('success')
    while o>0:
        no.append(o)
        o-=1
    print(no, o)
    
    context = {'usn': student.USN, 'number': no, 'count': len(no)}
    return render(request, 'student_dashboard/course_register_form.html', context)
