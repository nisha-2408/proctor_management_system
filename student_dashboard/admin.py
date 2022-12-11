from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.CGPA)
admin.site.register(models.Sem)
admin.site.register(models.courseRequest)
admin.site.register(models.StudentDetail)
