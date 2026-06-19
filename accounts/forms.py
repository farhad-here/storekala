from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

user = get_user_model()

class SignUpForm(UserCreationForm):
       class Meta:
              model = User
              fields = ['username', 'email', 'passwordOne', 'passwordtwo']
       def clean_email(self):
              email = self.cleaned_data.get('email')
              if User.objects.filter(email=email).exists():
                     raise forms.ValidationError('The email is not accurate use another one.')
              return email
