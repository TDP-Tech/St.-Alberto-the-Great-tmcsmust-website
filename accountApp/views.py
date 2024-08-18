# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from . forms import SignUpForm, EmailAuthenticationForm  #, UserLoginForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('welcome_page')  # Redirect to your home page
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associate the profile with the current user
            profile.save()
            return redirect('profile-list')
    else:
        form = ProfileForm()
    return render(request, 'profile_create.html', {'form': form})


@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

# @login_required
# def profile_detail(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     return render(request, 'profile_detail.html', {'profile': profile})
from django.core.exceptions import ObjectDoesNotExist

@login_required
def profile_detail(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return render(request, 'profile_not_found.html')
    return render(request, 'profile_detail.html', {'profile': profile})



@login_required
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-detail', pk=pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_update.html', {'form': form})


@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile-list')
    return render(request, 'profile_delete.html', {'profile': profile})
