from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
import re

from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes,force_str
from django.conf import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from student_dashboard.models import Student
from faculty_dashboard.models import Faculty


from .models import User
from .utils import generate_token
# Create your views here.




def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('authentication/activate.html', {
    'user': user,
    'domain': current_site,
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': generate_token.make_token(user)
    })

    send_mail(email_subject, email_body,settings.EMAIL_HOST_USER,[user.email])

def validateEmail(email):
    EmailRegex = r'^([a-z\d\.-]+)@bmsce.ac.in'
    return re.match(EmailRegex, email)

def validateEmailFaculty(email):
    EmailRegex = r'^([a-z]+).cse@bmsce.ac.in'
    return re.match(EmailRegex, email)

def validatePassword(password):
    passwordRegex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,10}$'
    return re.match(passwordRegex, password)

def student_signup(request):
    
    c=request.get_full_path()
    k = 'signin' in c or 'signup' in c
    context={'current_path': k}

    if request.method == 'POST':
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not validateEmail(email):
            messages.add_message(request, messages.ERROR,'Enter your BMSCE Mail')
            return render(request, 'student_signup.html', context,  status=409)
        
        if not validatePassword(password):
            messages.add_message(request, messages.ERROR,' Password must contain minimum eight and maximum 10 characters, at least one uppercase letter, one lowercase letter, one number and one special character')
            return render(request, 'student_signup.html', context,  status=409)
        
        if password != confirm_password:
            messages.add_message(request, messages.ERROR,'Password mismatch')
            return render(request, 'student_sign.html', context,  status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,'You are already Registered,SignIn!')
            return redirect(reverse('student_signin'))

        user=User.objects.create_user(email=email,name=name)
        details=Student()
        details.name=name
        details.USN=usn
        details.email=email
        details.save()
        user.set_password(password)
        user.save()
        send_activation_email(user,request)
        messages.add_message(request, messages.SUCCESS, 'We sent you an email to verify your account')
        return redirect(reverse('student_signin'))

    return render(request, 'student_signup.html', context)

def student_signin(request):
    c=request.get_full_path()
    k = 'signin' in c or 'signup' in c
    context={'current_path': k}
    if request.user.is_authenticated and not request.user.is_teacher :
        student=Student.objects.get(email=request.user.email)
        return redirect( 'student:dashboard', pk=student.USN)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        
        if user and user.is_teacher:
            messages.add_message(request,messages.ERROR,"Invalid credentials, try again")
            return render(request, 'student_signin.html', context,  status=409)

        if user and not user.is_email_verified:
            messages.add_message(request,messages.ERROR,"Student Email Not Verified! Check your Inbox ")
            return render(request, 'student_signin.html', context,  status=409)
                
        if not user:
            messages.add_message(request,messages.ERROR,"Invalid credentials, try again")
            return render(request, 'student_signin.html', context,  status=409)
        #messages.add_message(request, messages.SUCCESS,'Welcome {}'.format(user.name))
        login(request,user)
        # here edit
        student=Student.objects.get(email=email)
        if(student.proctor_id):
            return redirect( 'student:dashboard', pk=student.USN)
        else:
            #edit the message
            return HttpResponse("You do not have a proctor")
    return render(request, 'student_signin.html', context)


def signout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,'Successfully logged out')
    # edit here
    
    return redirect(reverse('home'))


def forgotPassword(request):
    if request.method == "POST":
        email = request.POST['email']
        try:
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if User.objects.filter(email=email).exists():
            current_site = get_current_site(request)
            email_subject = 'Reset your password'
            email_body = render_to_string('authentication/password/reset.html', {
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
            })
            send_mail(email_subject, email_body,settings.EMAIL_HOST_USER,[email])
            #messages.add_message(request, messages.SUCCESS,'Mail has been sent to your Registered Email address {}'.format(email))
            return redirect(reverse('password_reset_done'))
        else:
            messages.error(request,'Email address does not exist')
    
    return render(request,'authentication/password/forgotPassword.html')

def resetPassword(request,uidb64,token):
    try:
        userpk = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=userpk)
        if user:
            if request.method == "POST":
                password1 = request.POST['new_password']
                password2 = request.POST['new_password2']
                if password1 == password2:
                    user.password = make_password(password1)
                    user.save()
                    #messages.success(request,'Password has been reset successfully')
                    return redirect(reverse('password_reset_complete'))
                else:
                    return HttpResponse('Two Password did not match')
                
        else:
            return HttpResponse('Wrong URL')
    except Exception as e:
        return HttpResponse('Wrong URL')
    return render(request,'authentication/password/resetPassword.html')


def activate(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('student_signin'))

    return HttpResponse("Something wrong with your Link!")

def faculty_signin(request):
    c=request.get_full_path()
    k = 'signin' in c or 'signup' in c
    context={'current_path': k}
    if request.user.is_authenticated and request.user.is_teacher :
        return redirect('dashboard')
        
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = authenticate(request, email=email, password=password)

        if user and not user.is_email_verified:
            messages.add_message(request,messages.ERROR,"Faculty Email Not Verified! Check your Inbox ")
            return render(request, 'faculty_signin.html', context,  status=409,)
        
        if user and not user.is_teacher:
            messages.add_message(request,messages.ERROR,"Invalid credentials, try again")
            return render(request, 'faculty_signin.html', context,  status=409)
                
        if not user:
            messages.add_message(request,messages.ERROR,"Invalid credentials, try again")
            return render(request, 'faculty_signin.html', context,  status=409)
        #messages.add_message(request, messages.SUCCESS,'Welcome {}'.format(user.name))
        login(request,user)
        # here edit
        return redirect(reverse('dashboard'))
    return render(request, 'faculty_signin.html', context)

def faculty_signup(request):
    c=request.get_full_path()
    k = 'signin' in c or 'signup' in c
    print(k)
    context={'current_path': k}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not validateEmailFaculty(email):
            messages.add_message(request, messages.ERROR,'Only Faculty Mail allowed')
            return render(request, 'faculty_signup.html', context,  status=409)
        
        if not validatePassword(password):
            messages.add_message(request, messages.ERROR,' Password must contain minimum eight and maximum 10 characters, at least one uppercase letter, one lowercase letter, one number and one special character')
            return render(request, 'faculty_signup.html', context,  status=409)

        if password != confirm_password:
            messages.add_message(request, messages.ERROR,'Password mismatch')
            return render(request, 'faculty_signup.html', context,  status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,'You are already Registered,SignIn!')
            return redirect(reverse('faculty_signin'))

        user=User.objects.create_user(email=email,name=name)
        details=Faculty()
        details.name=name
        details.email=email
        details.save()
        user.set_password(password)
        user.is_teacher=True
        user.save()
        print(user)
        send_activation_email(user,request)
        messages.add_message(request, messages.SUCCESS, 'We sent you an email to verify your account')
        return redirect(reverse('faculty_signin'))
    return render(request, 'faculty_signup.html', context)

def homepage(request):
    context = {'current_path': request.get_full_path()}
    return render(request, "index.html", context)


def dashboard(request):
    return render(request, 'dashboard.html')
