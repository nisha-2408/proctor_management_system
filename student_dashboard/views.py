from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from student_dashboard.models import Student, courseRequest, Sem, StudentDetail, Fastrack
from .forms import StudentDetailsForm

# Create your views here.
@login_required
def dashboard(request, pk):
    student=Student.objects.get(email=request.user.email)
    if(StudentDetail.objects.filter(USN=student.USN).exists()):
        s_info = StudentDetail.objects.get(USN=student.USN)
    else:
        s_info = 0
    number=courseRequest.objects.filter(student_usn=student.USN)
    sem=student.current_sem
    if(pk!=student.USN):
        return HttpResponse("Not allowd")
    courses = models.Sem.objects.filter(USN=pk, sem=sem)
    fastrack = models.Fastrack.objects.filter(USN=pk, is_active=True)
    length = fastrack.count()
    context = {'courses': courses, 'req': number.count(), 'sem': sem, 's_info': s_info, 'student': student, 'usn': student.USN, 'fast_count': length, 'fasttrack': fastrack}
    return render(request, 'student_dashboard/dashboard.html', context)


@login_required
def dashboard_marks(request, pk):
    student=Student.objects.get(email=request.user.email)
    number=courseRequest.objects.filter(student_usn=student.USN)
    sem=student.current_sem
    if(pk!=student.USN):
        return HttpResponse("Not allowd")
    courses = models.Sem.objects.filter(USN=pk, sem=sem)
    print(courses)
    context = {'courses': courses, 'req': number.count(), 'sem': sem,}
    return render(request, 'student_dashboard/course_marks.html', context)

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
        return redirect( 'student:dashboard', pk=student.USN)
    while o>0:
        no.append(o)
        o-=1
    print(no, o)
    
    context = {'usn': student.USN, 'number': no, 'count': len(no)}
    return render(request, 'student_dashboard/course_register_form.html', context)

@login_required
def studentDetails(request):
    student=Student.objects.get(email=request.user.email)
    if(StudentDetail.objects.filter(USN=student.USN).exists()):
        s_info = StudentDetail.objects.get(USN=student.USN)
    else:
        s_info = 0
    print(s_info)
    submitted = False
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.instance.user = student
            form.save()
            obj=form.cleaned_data
            studeob=StudentDetail(USN=obj['USN'], father_name=obj['father_name'], mother_name=obj['mother_name'], date_of_birth=obj['date_of_birth'], permanent_address=obj['permanent_address'], current_address=obj['current_address'], phone_number=obj['phone_number'],
                                  blood_group=obj['blood_group'], father_occupation=obj['father_occupation'], mother_occupation=obj['mother_occupation'], father_phone_number=obj['father_phone_number'], mother_phone_number=obj['mother_phone_number'], 
                                  father_email=obj['father_email'], mother_email=obj['mother_email'], guardian_name=obj['guardian_name'], guardian_email=obj['guardian_email'], guardian_phone_number=obj['guardian_phone_number'],
                                  class_10th_school=obj['class_10th_school'], class_10th_percentage=obj['class_10th_percentage'], class_10th_board=obj['class_10th_board'], class_10th_year=obj['class_10th_year'], 
                                  class_12th_school=obj['class_12th_school'], class_12th_percentage=obj['class_12th_percentage'], class_12th_board=obj['class_12th_board'], class_12th_year=obj['class_12th_year'], 
                                  class_Diploma_school=obj['class_Diploma_school'], class_Diploma_percentage=obj['class_Diploma_percentage'], class_Diploma_board=obj['class_Diploma_board'], class_Diploma_year=obj['class_Diploma_year'], 
                                  )
            #print(form.cleaned_data)
            studeob.save()
            return HttpResponseRedirect('/student/add_student_details/?submitted=True')
    else:
        if s_info != 0 :
            form = StudentDetailsForm(instance=s_info)
        else :
            form = StudentDetailsForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'student_dashboard/student_details_form.html', {'form':form, 'submitted':submitted, 's_info':s_info, 'usn': student.USN})


@login_required
def editCourseDetails(request):
    student=Student.objects.get(email=request.user.email)
    courses=Sem.objects.filter(USN=student.USN, sem=student.current_sem)
    o=courses.count()
    if request.method=="POST":
        for course in courses:
            course.courseCode=request.POST['code%s' %(o)]
            course.courseName=request.POST['name%s' %(o)]
            course.credit=request.POST['credits%s' %(o)]
            course.registration=request.POST['reg%s' %(o)]
            course.attemptNumber=request.POST['attempt%s' %(o)]
            course.save()
            o-=1
        return redirect( 'student:dashboard', pk=student.USN)
    context={'courses': courses}
    return render(request, 'student_dashboard/course_edit_form.html', context)

@login_required
def updateCourseDetails(request):
    student=Student.objects.get(email=request.user.email)
    courses=Sem.objects.filter(USN=student.USN, sem=student.current_sem)
    o=courses.count()
    if request.method=="POST":
        for course in courses:
            attendence=float(request.POST['attendance%s' %(o)])
            cie=float(request.POST['cie%s' %(o)])
            see=float(request.POST['see%s' %(o)])
            gradepoints=float(request.POST['gp%s' %(o)])
            if attendence>100 or attendence<0 or cie>50 or cie<0 or see>100 or see<0 or gradepoints<0 or gradepoints>10:
                messages.add_message(request, messages.ERROR,'Enter proper details!')
                return redirect('student:update')
            course.attendance=attendence
            course.CIE=cie
            course.SEE=see
            course.GradePoints=gradepoints
            course.save()
            o-=1
        return redirect( 'student:dashboard', pk=student.USN)
    context={'courses': courses}
    return render(request, 'student_dashboard/course_update_form.html', context)