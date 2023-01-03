from django.forms import ModelForm
from . import models
from .models import StudentDetail
from django import forms

class Courses(models.Sem):
    o=5


class StudentDetailsForm(ModelForm):
    class Meta:
        model= StudentDetail
        fields= 'USN','father_name','mother_name','date_of_birth','permanent_address','current_address','phone_number','blood_group','father_occupation','mother_occupation','father_phone_number','mother_phone_number','father_email','mother_email','guardian_name','guardian_phone_number','guardian_email','class_10th_school','class_10th_board','class_10th_percentage','class_10th_year','class_12th_school','class_12th_board','class_12th_percentage','class_12th_year','class_Diploma_school','class_Diploma_board','class_Diploma_percentage','class_Diploma_year'
        widgets = {
            'USN': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'father_name': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'mother_name': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'permanent_address': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'current_address': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'phone_number': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'blood_group': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'father_occupation': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'mother_occupation': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'father_phone_number': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'mother_phone_number': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'father_email': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'mother_email': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'guardian_name': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'guardian_phone_number': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'guardian_email': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_10th_school': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_10th_board': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_10th_percentage': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_10th_year': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_12th_school': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_12th_board': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_12th_percentage': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_12th_year': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_Diploma_school': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_Diploma_board': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_Diploma_percentage': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
            'class_Diploma_year': forms.TextInput(attrs={'class': 'position form-control border','style':'margin-bottom: 1%; width: 80%;'}),
        }