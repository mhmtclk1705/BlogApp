from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .forms import UserForm, UserProfileForm,UserUpdateProfileForm
from django.contrib.auth.models import User
from .models import UserProfile
def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    # logout işlemi yapılıyor
    messages.success(request, 'You are logged out')
    logout(request)
    # logout işlemi yapıldıktan sonra login sayfasına yönlendiriliyor
    return redirect('home')

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            # username = form_user.cleaned_data.get('username')
            login(request, user)
            messages.success(request, 'Register Successfull')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfull')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    context = {
        'form': form,
        
    }
    return render(request, 'users/user_login.html', context)


def profile(request):
    form = UserUpdateProfileForm(instance=request.user)
    form_profile = UserProfileForm(instance=request.user.userprofile)
    if request.method == 'POST':
        form = UserUpdateProfileForm(request.POST, request.FILES, instance=request.user)
        form_profile = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and form_profile.is_valid():
            form.save()
            form_profile.save()
            messages.success(request, 'Profile Updated')
            return redirect('home')
    else:
        form = UserUpdateProfileForm(instance=request.user)
        form_profile = UserProfileForm(instance=request.user.userprofile)
    context = {
        'form': form,
        'form_profile': form_profile

    }

    return render(request, 'users/profile.html',context)