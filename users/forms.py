from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'confirm_password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'country', 'gender', 'description', 'date_of_birth', 'image')

        labels = {
            'full_name': 'ФИО',
            'email': 'Email',
            'country': 'Страна',
            'gender': 'Пол',
            'description': 'Описание',
            'education': 'Образование',
            'date_of_birth': 'Дата рождения',
            'image': 'Изображение',
        }
