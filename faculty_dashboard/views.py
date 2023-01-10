from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student_dashboard.models import Student, StudentDetail, Sem, Fastrack
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import openpyxl

# Create your views here.
@login_required
def dashboard(request):
    faculty = Faculty.objects.get(email=request.user.email)
    students = Student.objects.filter(proctor_id=faculty)
    context = {'faculty': faculty, 'students': students}
    return render(request, 'faculty_dashboard/dashboard.html', context)

def sendFillMail(request, message, name, emails):
    template = render_to_string('faculty_dashboard/send_fill.html', {'message': message, 'name': name})
    email = EmailMessage(
                message,
                template,
                settings.EMAIL_HOST_USER,
                [emails],
                # fail_silently=False,
            )
    email.send()

def studentDetails(request, pk):
    if StudentDetail.objects.filter(USN=pk).exists():
        s_info = StudentDetail.objects.get(USN=pk)
    else :
        s_info = 0
    student = Student.objects.get(USN=pk)
    if request.method == 'POST':
        message = request.POST['email-text']
        sendFillMail(request, message, 'Sudeep' ,student.email)
        return redirect('faculty:dashboard')
    courses = Sem.objects.filter(sem=student.current_sem, USN=pk)
    marks = courses[0].CIE == None
    fastrack = Fastrack.objects.filter(USN=pk, is_active=True)
    length = fastrack.count()
    context = {'s_info': s_info, 'courses': courses, 'fasttrack': fastrack, 'fast_count': length, 'email': student.email, 'usn': student.USN, 'marks': marks}
    return render(request, 'faculty_dashboard/student_details.html', context)

def approve(request, pk):
    s_info = StudentDetail.objects.get(USN=pk)
    s_info.isApproved = True
    s_info.save()
    return redirect('faculty:student-details', pk=pk)

def courseApprove(request, pk, course_id):
    course = Sem.objects.get(USN=pk, courseCode=course_id)
    course.is_approved = True
    course.save()
    return redirect('faculty:student-details', pk=pk)

def courseReject(request, emails):
    student=Student.objects.get(email=emails)
    message = 'Looks like there is a mistake in your registered courses, check out the unapproved courses and update it'
    faculty = Faculty.objects.get(email=request.user.email)
    name = faculty.name
    template = render_to_string('faculty_dashboard/send_fill.html', {'message': message, 'name': name})
    email = EmailMessage(
        
                message,
                template,
                settings.EMAIL_HOST_USER,
                [emails],
                # fail_silently=False,
                
            )
    email.send()
    return redirect('faculty:student-details', pk=student.USN)

def addStudents(request):
    if request.method == "POST":
        excel_file = request.FILES['excel']
        print(excel_file)
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        excel_data = list()
        data = []
        row_data = list()
        for cols in worksheet.iter_cols():
            for cell in cols:
                if str(cell.value) == 'USN':
                    data = cols
                    break
                else:
                    continue
            if data != '':
                break
        for cell in data:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
        print(len(row_data))
        faculty = Faculty.objects.get(email=request.user.email)
        for usn in row_data:
            if usn == 'USN':
                continue
            else:
                student = Student.objects.get(USN=usn)
                student.proctor_id = faculty
                student.save()
        return HttpResponse("Hola")
    return render(request, 'faculty_dashboard/add_students.html')