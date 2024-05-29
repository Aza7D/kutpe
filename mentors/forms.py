from django import forms

from .models import MentorTypeUser


class MentorProfileForm(forms.ModelForm):

    class Meta:
        model = MentorTypeUser
        fields = ('subjects', 'description', 'phone_number', 'city', 'hourly_rate', 'format', 'education',
                  'instagram', 'telegram', 'image')
        labels = {
            'subjects': 'Предметы',
            'description': 'Описание',
            'phone_number': 'Номер телефона',
            'city': 'Город',
            'hourly_rate': 'Почасовая ставка',
            'format': 'Формат',
            'education': 'Образование',
            'instagram': 'Instagram',
            'telegram': 'Telegram',
            'image': 'Картина',
        }


class ContactWithMentorForm(forms.Form):
    student_name = forms.CharField(max_length=100, label="Ваше имя")
    phone_number = forms.CharField(max_length=255, label="Номер телефона")
