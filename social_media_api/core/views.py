from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from posts.models import Post, Trend
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .forms import PostForm  # Assuming you create a form for posts


# Redirect the root URL to the login page if the user is not logged in
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # If the user is already logged in, go to home page
    return redirect('login')  # Otherwise, go to the login page
# Home page view (Only accessible for logged-in users)
@login_required
def home(request):
    posts = Post.objects.all()
    trends = Trend.objects.all()  # Replace with your logic for trending content
    return render(request, 'core/home.html', {
        'posts': posts,
        'trends': trends,
    })

# Login view (Displays login form and handles user authentication)
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# Register view (Displays registration form and handles user creation)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# Password reset view (Displays form and handles password reset request)
def reset_password_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)  # Sends a reset email to the user
            return redirect('login')  # Redirect to login page after reset request
    else:
        form = PasswordResetForm()
    return render(request, 'core/reset_password.html', {'form': form})

# You can also use Django's built-in password reset view
# URL pattern for the password reset view would be like this:
# path('reset-password/', PasswordResetView.as_view(), name='password_reset')



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the current user as the author
            post.save()
            return redirect('home')  # Redirect back to home after posting
    else:
        form = PostForm()

    return render(request, 'core/create_post.html', {'form': form})
