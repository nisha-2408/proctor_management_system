from django.forms import ModelForm
from . import models
from .models import StudentDetail

class Courses(models.Sem):
    o=5


class StudentDetailsForm(ModelForm):
    class Meta:
        model= StudentDetail
        fields= '__all__'