from django.db import models
from faculty_dashboard.models import Faculty

# Create your models here.

class Student(models.Model):
    USN= models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email=models.EmailField()
    proctor_id=models.ForeignKey(Faculty, null=True, blank=True, on_delete=models.DO_NOTHING)
    current_sem=models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    #personal details
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.USN

class StudentDetail(models.Model):
    USN=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    permanent_address=models.TextField()
    current_address=models.TextField()
    phone_number=models.CharField(max_length=10)
    blood_group=models.CharField(max_length=3)

    father_name=models.CharField(max_length=200)
    mother_name=models.CharField(max_length=200)
    father_occupation=models.CharField(max_length=200, null=True, blank=True)
    mother_occupation=models.CharField(max_length=200, null=True, blank=True)
    father_phone_number=models.CharField(max_length=10)
    mother_phone_number=models.CharField(max_length=10)
    father_email=models.EmailField()
    mother_email=models.EmailField()

    guardian_name=models.CharField(max_length=200)
    guardian_phone_number=models.CharField(max_length=10)
    guardian_email=models.EmailField()

    class_10th_school=models.CharField(max_length=200)
    class_10th_board=models.CharField(max_length=200)
    class_10th_percentage=models.DecimalField(max_digits=5, decimal_places=2)
    class_10th_year=models.DecimalField(max_digits=4, decimal_places=0)

    class_12th_school=models.CharField(max_length=200)
    class_12th_board=models.CharField(max_length=200)
    class_12th_percentage=models.DecimalField(max_digits=5, decimal_places=2)
    class_12th_year=models.DecimalField(max_digits=4, decimal_places=0)

    class_Diploma_school=models.CharField(max_length=200, null=True, blank=True)
    class_Diploma_board=models.CharField(max_length=200, null=True, blank=True)
    class_Diploma_percentage=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    class_Diploma_year=models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)

    # class Meta:
    #     ordering = ['USN']
    def __str__(self):
        return self.USN
    

class CGPA(models.Model):
    USN=models.CharField(max_length=10)
    total_credits_registered=models.DecimalField(max_digits=2, decimal_places=0)
    total_credits_earned=models.DecimalField(blank=True, max_digits=2, decimal_places=0)
    cgpa=models.DecimalField(max_digits=1, decimal_places=0)
    sem=models.DecimalField(max_digits=1, decimal_places=0)
    class Meta:
        ordering = ['USN']
    
class courseRequest(models.Model):
    faculty = models.OneToOneField(Faculty, on_delete=models.DO_NOTHING)
    no_subjects = models.IntegerField(max_length=1)
    student_usn = models.CharField(max_length=10)
    sem = models.IntegerField()
    
class Sem(models.Model):
    USN=models.CharField(max_length=10)
    sem=models.IntegerField()
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.TextField()
    registration=models.TextField() #regular or re registered
    attemptNumber=models.FloatField(blank=True, null=True)
    attendance=models.FloatField(blank=True, null=True)
    CIE=models.FloatField(blank=True, null=True)
    SEE=models.FloatField(max_length=1, blank=True, null=True)
    GradePoints=models.FloatField(blank=True, null=True)
    is_approved=models.BooleanField(default=False)
    is_marks_approved = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    #courses to be cleared if any
    #proctor remarks
    
class Fastrack(models.Model):
    USN=models.CharField(max_length=10)
    sem=models.IntegerField()
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.TextField()
    registration=models.TextField() #regular or re registered
    attemptNumber=models.FloatField(blank=True, null=True)
    attendance=models.FloatField(blank=True, null=True)
    CIE=models.FloatField(blank=True, null=True)
    SEE=models.FloatField(max_length=1, blank=True, null=True)
    GradePoints=models.FloatField(blank=True, null=True)
    # is_approved=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #courses to be cleared if any
    #proctor remarks
    