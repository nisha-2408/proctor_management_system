from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
