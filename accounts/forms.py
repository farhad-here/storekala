from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    is_seller = forms.BooleanField(required=False, label='I want to be a Seller', widget=forms.CheckboxInput(attrs={
        'class': 'seller-checkbox',
        'style': 'width:20px;height:20px;accent-color:firebrick;'
    }))

    class Meta:
        model = get_user_model()
        fields = ['phone','first_name','last_name', 'password1', 'password2', 'is_seller']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        User = get_user_model()
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError('The phone is not accurate use another one.')
        return phone

class IncreaseBalanceForm(forms.Form):
       amount = forms.DecimalField(
       min_value=1000,
       max_digits=10,
       decimal_places=0,
       label='Amount'
    )
       
class PaymentForm(forms.Form):
    AMOUNT_CHOICES = [
        (50000,  '۵۰,۰۰۰ تومان'),
        (100000, '۱۰۰,۰۰۰ تومان'),
        (200000, '۲۰۰,۰۰۰ تومان'),
        (500000, '۵۰۰,۰۰۰ تومان'),
    ]
    amount = forms.ChoiceField(
        choices=AMOUNT_CHOICES,
        label='مقدار شارژ'
    )
    custom_amount = forms.IntegerField(
        required=False,
        min_value=10000,
        label='مقدار دلخواه (تومان)'
    )

    def clean(self):
        cleaned_data = super().clean()
        custom = cleaned_data.get('custom_amount')
        if custom:
            cleaned_data['final_amount'] = custom
        else:
            cleaned_data['final_amount'] = int(cleaned_data.get('amount', 0))
        return cleaned_data
    

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='شماره تلفن',
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره تلفن خود را وارد کنید'
        })
    )
    
    def clean(self):
        phone_number = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if phone_number is not None and password:
            # احراز هویت با شماره تلفن
            self.user_cache = authenticate(
                self.request, 
                username=phone_number, 
                password=password
            )
            
            if self.user_cache is None:
                raise forms.ValidationError(
                    'شماره تلفن یا رمز عبور اشتباه است',
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data