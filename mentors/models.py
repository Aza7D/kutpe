from django.db import models
from django.utils import timezone
from users.models import User

CITY_CHOICES = [
    ('Almaty', 'Алматы'),
    ('Nur-Sultan', 'Нур-Султан (Астана)'),
    ('Shymkent', 'Шымкент'),
    ('Karaganda', 'Караганда'),
    ('Aktobe', 'Актобе'),
    ('Taraz', 'Тараз'),
    ('Pavlodar', 'Павлодар'),
    ('Ust-Kamenogorsk', 'Усть-Каменогорск'),
    ('Semey', 'Семей'),
    ('Atyrau', 'Атырау'),
    ('Kostanay', 'Костанай'),
    ('Petropavl', 'Петропавловск'),
    ('Kyzylorda', 'Кызылорда'),
    ('Aktau', 'Актау'),
    ('Uralsk', 'Уральск'),
    ('Kokshetau', 'Кокшетау'),
    ('Taldykorgan', 'Талдыкорган'),
    ('Turkestan', 'Туркестан'),
    ('Othen', 'Другое')
]

FORMAT_CHOICES = [
    ('online', 'Онлайн'),
    ('offline', 'Оффлайн'),
]

EDUCATION_CHOICES = [
    ('online', 'Онлайн'),
    ('offline', 'Оффлайн'),
]


class MentorTypeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=200)
    description = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=1000, blank=True, null=True)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    education = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='media/mentors', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.handle_custom_value('city', CITY_CHOICES)
        self.handle_custom_value('format', FORMAT_CHOICES)

        super(MentorTypeUser, self).save(*args, **kwargs)

    def handle_custom_value(self, field_name, choices):
        field_value = getattr(self, field_name)
        custom_field_name = 'custom_' + field_name

        if field_value and field_value not in [choice[0] for choice in choices]:
            setattr(self, custom_field_name, field_value)
            setattr(self, field_name, None)

    def __str__(self):
        return self.user.email


class ContactWithMentor(models.Model):
    mentor = models.ForeignKey(MentorTypeUser, on_delete=models.CASCADE, related_name='contacts')
    student_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
