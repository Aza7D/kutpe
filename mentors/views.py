from django.shortcuts import render, redirect

from .forms import ContactWithMentorForm, MentorProfileForm
from .models import MentorTypeUser


def manage_mentor_profile(request):
    user = request.user
    try:
        mentor_profile = MentorTypeUser.objects.get(user=user)
    except:
        mentor_profile = None

    if request.method == 'POST':
        form = MentorProfileForm(request.POST, request.FILES, instance=mentor_profile)
        if form.is_valid():
            mentor_profile = form.save(commit=False)
            mentor_profile.user = user
            mentor_profile.save()
            return redirect('profile')
    else:
        form = MentorProfileForm(instance=mentor_profile)

    return render(request, 'profile/manage_mentor_profile.html', {'form': form})


def mentor_detail(request, mentor_id):
    mentor = MentorTypeUser.objects.get(pk=mentor_id)
    return render(request, 'profile/mentor_detail.html', {'mentor': mentor})


def leave_contact(request, mentor_id):
    mentor = MentorTypeUser.objects.get(id=mentor_id)

    if request.method == 'POST':
        form = ContactWithMentorForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            phone_number = form.cleaned_data['phone_number']
            mentor.contacts.create(student_name=student_name, phone_number=phone_number)
            return redirect('home')

    else:
        form = ContactWithMentorForm()

    return render(request, 'profile/leave_contact.html', {'form': form, 'mentor': mentor})


def mentors_list(request):
    mentors = MentorTypeUser.objects.all()
    return render(request, 'mentors/mentors_list.html', {'mentors': mentors})
