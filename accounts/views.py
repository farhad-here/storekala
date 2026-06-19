from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm

def signup_view(request):
       if request.user.is_authenticated:
              return redirect('homepage')
       form = SignUpForm(request.POST or None)
       if form.is_valid():
              user = form.save()
              login(request, user)
              return redirect('homepage')
       return render(request, 'registration/signup.html', {'form':form})


def login_view(request):
       if request.user.is_authenticated:
              return redirect('homepage')
       form = AuthenticationForm(request, data=request.POST or None)
       if form.is_valid():
              user = form.get_user()
              login(request, user)
              return redirect(request.GET.get('next', 'homepage'))
       return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    if request.method == 'POST': 
       logout(request)
    return redirect('homepage')