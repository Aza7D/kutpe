# views.py
from django.shortcuts import render, redirect
from .forms import StudentInfoForm


def student_info(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request, 'events/ticket.html', {'student': student})
    else:
        form = StudentInfoForm()

    return render(request, 'events/student_info.html', {'form': form})
