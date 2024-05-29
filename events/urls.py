from django.urls import path

from .views import student_info

urlpatterns = [
    path('student_info/', student_info, name='student_info'),
]
