from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse

def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    """Handle user login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            # Redirect to 'next' if present in GET params
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'blog/login.html')

@login_required
def profile_view(request):
    """Allow user to view and update their profile"""
    if request.method == 'POST':
        email = request.POST.get('email', request.user.email)
        request.user.email = email
        request.user.save()
        messages.success(request, "Profile updated successfully!")
    return render(request, 'blog/profile.html', {'user': request.user})

def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')
