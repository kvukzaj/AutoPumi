from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login as lg, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from AutopumiAPP.forms import contact_form
from AutopumiAPP.forms import ContactForm
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def Rrethnesh(request):
    return render(request, 'Rreth nesh.html')

@login_required
def kontakt(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
    else:
        form = contact_form()
    return render(request, 'kontakt.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            user = authenticate(request=request, username=email, password=password)
            if user:
                lg(request, user)
                return redirect('/home/')
            else:
                messages.error(request, "Invalid Credentials!")
                return redirect('/login/')
        else:
            messages.error(request, "Email and password are required.")
            return redirect('/login/')
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login/')


def login_emp(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    if email and password:
        user = authenticate(request=request, username=email, password=password)
        if user:
            login(request=request, user=user)
            return redirect('home/')
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('login/')
    else:
        messages.error(request, "Email and password are required.")
        return redirect('login/')