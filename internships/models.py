from django.db import models
from django.utils import timezone

from users.models import User


class Internship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255, verbose_name='Название организации')
    position = models.CharField(max_length=255, verbose_name='Должность')
    description = models.TextField(verbose_name='Описание стажировки')
    image = models.ImageField(upload_to='media/internships', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = models.Manager()

    def __str__(self):
        return f'{self.organization_name} - {self.position}'

    class Meta:
        verbose_name = 'Стажировка'
        verbose_name_plural = 'Стажировки'
