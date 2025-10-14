from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages   
from .models import usignup
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

def index(request):
    user_name = request.session.get('user_name')  
    return render(request, 'index.html', {'user_name': user_name})

def profile(request):
    user_name = request.session.get('user_name')
    if not user_name:
        return redirect('login')  
    return render(request, 'profile.html', {'user_name': user_name})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = usignup.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.full_name
                messages.success(request, f'Welcome back, {user.full_name}!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid password!')
        except usignup.DoesNotExist:
            messages.error(request, 'No account found with this email!')

    return render(request, 'login.html')


def logout(request):
    request.session.flush()  
    messages.success(request, 'You have been logged out successfully.')
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if usignup.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered!')
        else:
            user = usignup(
                full_name=full_name,
                email=email,
                password=make_password(password)  
            )
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')

    return render(request, 'signup.html')

def courses(request):
    return render(request, 'courses.html')
