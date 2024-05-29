from django.shortcuts import render, redirect

from .forms import InternshipForm
from .models import Internship


def create_internship(request):
    user = request.user
    try:
        internship = Internship.objects.get(user=user)
    except:
        internship = None

    if request.method == 'POST':
        form = InternshipForm(request.POST, request.FILES, instance=internship)
        if form.is_valid():
            internship = form.save(commit=False)
            internship.user = user
            internship.save()
            return redirect('profile')
    else:
        form = InternshipForm(instance=internship)

    return render(request, 'profile/create_internship.html', {'form': form})


def internships_list(request):
    internships = Internship.objects.all()
    return render(request, 'internships/internships_list.html', {'internships': internships})
