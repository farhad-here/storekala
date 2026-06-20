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