from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Products

from internships.models import Internship
from mentors.models import MentorTypeUser


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                user = form.save(commit=False)
                user.username = form.cleaned_data['email']
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Пароли не совпадают.")
        else:
            messages.error(request, "Форма недействительна. Пожалуйста, исправьте ошибки.")
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'form': form})


def home(request):
    mentors = MentorTypeUser.objects.all()[:4]
    internships = Internship.objects.all()[:4]
    context = {'mentors': mentors, 'internships': internships}
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


def first_page(request):
    return render(request, 'user/first_page.html')


def account_type(request):
    return render(request, 'user/account_type.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Неправильный логин или пароль.")
            return render(request, 'user/login.html')
    return render(request, 'user/login.html')


def profile_view(request):
    user = request.user
    mentor_profile = MentorTypeUser.objects.filter(user=user).first()
    internship = Internship.objects.filter(user=user).first()

    is_mentor = mentor_profile is not None
    is_internship = internship is not None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'user': user,
        'mentor_profile': mentor_profile,
        'form': form,
        'is_mentor': is_mentor,
        'is_internship': is_internship,
        'internship': internship
    }

    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'profile/edit_profile.html', {'form': form})

def products(request):
    products = Products.objects.all()
    if products:
        return render(request, 'products.html', {'products': products})
    else:
        return redirect('home')


