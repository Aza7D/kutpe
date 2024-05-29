from django.urls import path

from .views import (create_internship,
                    internships_list)

urlpatterns = [
    path('internships_list/', internships_list, name='internships_list'),
    path('create_internship/', create_internship, name='create_internship'),
]
