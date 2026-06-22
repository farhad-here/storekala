from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    is_seller = forms.BooleanField(required=False, label='I want to be a Seller')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'is_seller']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is not accurate use another one.')
        return email
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