from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserExtension

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validation
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/auth/register/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('/auth/register/')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('/auth/register/')

        # Create user
        user = User.objects.create_user(username=username,first_name = fullname, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, 'User registered successfully. Please login.')
        return redirect('/auth/login/')

    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            user_type = user.userextension.user_type

            if user_type == 'normal':
                return redirect('/home/problems/')
            elif user_type == 'setter':
                return redirect('/home/problems/')
            elif user_type == 'admin':
                return redirect('/admin/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/auth/login/')

    template = loader.get_template('login.html')
    context ={}
    return HttpResponse(template.render(context,request))


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('/auth/login/')

@login_required
def profile_view(request):
    user = request.user
    try:
        user_extension = user.userextension
    except UserExtension.DoesNotExist:
        user_extension = None  # or handle fallback

    context = {
        'user': user,
        'user_extension': user_extension
    }
    return render(request, 'profile.html', context)