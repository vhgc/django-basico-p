""" User views."""
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# models
from django.contrib.auth.models import User
from users.models import Profile

# Exceptions
from django.db.utils import IntegrityError

@login_required
def update_profile(request):
    """ Update user's profile. """
    return render(request, 'users/update_profile.html')


def login_view(request):
    """ Login view."""
    if request.method == 'POST':
        # print('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

def signup(request):
    """ Signup view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_con = request.POST['password_confirmation']

        if password != password_con:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match!'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'The username already exist!'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect(request, 'login')

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    """ Login user."""
    logout(request)
    return redirect('login')