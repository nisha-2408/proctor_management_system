from django.db import models
from faculty_dashboard.models import Faculty

# Create your models here.

class Student(models.Model):
    USN= models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email=models.EmailField()
    proctor_id=models.OneToOneField(Faculty, null=True, blank=True, on_delete=models.DO_NOTHING)
    #personal details
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.USN
