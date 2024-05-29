# forms.py
from django import forms
from .models import StudentInfo


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['full_name', 'university', 'course', 'specialty', 'purpose']
