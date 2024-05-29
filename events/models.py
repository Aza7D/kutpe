# models.py
from django.db import models


class StudentInfo(models.Model):
    full_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course = models.IntegerField()
    specialty = models.CharField(max_length=255)
    purpose = models.TextField()

    def __str__(self):
        return self.full_name
