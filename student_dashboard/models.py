from django.db import models
from faculty_dashboard.models import Faculty

# Create your models here.

class Student(models.Model):
    USN= models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email=models.EmailField()
    proctor_id=models.OneToOneField(Faculty, null=True, blank=True, on_delete=models.DO_NOTHING)
    current_sem=models.DecimalField(max_digits=1, decimal_places=0)
    #personal details
    class Meta:
        ordering = ['name']
        
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
    attemptNumber=models.TextField(blank=True, null=True)
    attendance=models.TextField(blank=True, null=True)
    CIE=models.TextField(blank=True, null=True)
    SEE=models.CharField(max_length=1, blank=True, null=True)
    GradePoints=models.TextField(blank=True, null=True)
    #courses to be cleared if any
    #proctor remarks
    