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
    
    
class Sem1(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )
    #courses to be cleared if any
    #proctor remarks
    
class Sem2(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )

class Sem3(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )

class Sem4(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )
    
class Sem5(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )
    
class Sem6(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )
    
class Sem7(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )
    
class Sem8(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )
    
class FastTrack(models.Model):
    USN=models.CharField(max_length=10)
    #cycle=models.CharField(max_length=50)
    courseName=models.TextField()
    courseCode=models.TextField() #can be changed to charfield
    credit=models.DecimalField(max_digits=3, decimal_places=2)
    registration=models.TextField() #regular or re registered
    attemptNumber=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    attendance=models.DecimalField(max_digits=5, blank=True, decimal_places=2)
    CIE=models.DecimalField(max_digits=2, blank=True, decimal_places=2)
    SEE=models.CharField(max_length=1)
    GradePoints=models.DecimalField(max_digits=2, decimal_places=2, )