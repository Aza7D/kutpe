from django import forms

from .models import Internship


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ('organization_name', 'position', 'description', 'image')
        labels = {
            'organization_name': 'Наименование организации',
            'position': 'Должность',
            'description': 'Описание',
            'image': 'Изображение'
        }
