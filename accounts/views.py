from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, IncreaseBalanceForm, PaymentForm
from .models import User, Profile 
from django.contrib import messages

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_seller = form.cleaned_data.get('is_seller', False)
        user.save()
        user.backend = 'accounts.backends.EmailOrUsernameBackend'
        login(request, user)
        return redirect('homepage')

    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect(request.GET.get('next', 'homepage'))

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
       if request.method == 'POST':
              logout(request)
              return render(request, 'registration/logged_out.html')
       return redirect('homepage')


@login_required
def customer_panel(request):
       profile, created = Profile.objects.get_or_create(user=request.user)
       cart = request.session.get('cart', {})    
       if request.method == 'POST':
           form = IncreaseBalanceForm(request.POST)
           if form.is_valid():
               amount = form.cleaned_data['amount']
               profile.balance += amount
               profile.save()
               messages.success(request, f'{amount} تومان به موجودی اضافه شد.')
               return redirect('customer_panel')
       else:
           form = IncreaseBalanceForm()   
       return render(request, 'accounts/customer_panel.html', {
           'profile': profile,
           'form': form,
           'cart_count': sum(cart.values()),
       })


@login_required
def payment_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['final_amount']
            profile.balance += amount
            profile.save()
            messages.success(request, f'✅ {amount:,} تومان با موفقیت به حساب شما اضافه شد.')
            return redirect('customer_panel')
    else:
        form = PaymentForm()

    return render(request, 'accounts/payment.html', {
        'form': form,
        'profile': profile,
    })