from django.urls import path
from .views import (manage_mentor_profile,
                    mentor_detail, leave_contact,
                    mentors_list)

urlpatterns = [
    path('mentors_list/', mentors_list, name='mentors_list'),
    path('become_mentor/', manage_mentor_profile, name='become_mentor'),
    path('mentor_detail/<int:mentor_id>/', mentor_detail, name='mentor_detail'),
    path('mentor/<int:mentor_id>/leave_contact/', leave_contact, name='leave_contact'),
]
