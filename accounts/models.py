from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):
       def _create_user(self, email, username, password=None, **extra_fields):
              if not email:
                     raise ValueError('Inserting Email is necessary')
              if not username:
                     raise ValueError('Inserting username is necessary')
              email = self.normalize_email(email)
              user = self.model(email=email, username=username, **extra_fields)
              user.set_password(password)
              user.save(using=self._db)
              return user
       def create_user(self, email, username, password=None, **extra_fields):
              extra_fields.setdefault('is_staff', False)
              extra_fields.setdefault('is_active', True)
              return self._create_user(email, username, password, **extra_fields)
       
       def create_superuser(self, email, username, password, **extra_fields):
              extra_fields.setdefault('is_staff', True)
              extra_fields.setdefault('is_active', True)
              extra_fields.setdefault('is_superuser', True)
              if extra_fields.get('is_active') is not True:
                     raise ValueError('superuser mush have is_active=True')
              if extra_fields.get('is_staff') is not True:
                     raise ValueError('superuser mush have is_staff=True')
              if extra_fields.get('is_superuser') is not True:
                     raise ValueError('superuser mush have is_superuser=True')

              return self._create_user(email, username, password, **extra_fields)
       
  
       
class User(AbstractBaseUser, PermissionsMixin):
       email = models.EmailField(unique=True)
       username = models.CharField(max_length=50, unique=True)
       is_active = models.BooleanField(default=True)
       is_staff = models.BooleanField(default=False)
       is_seller = models.BooleanField(default=False)

       objects = CustomUserManager()
       USERNAME_FIELD = 'email'        
       REQUIRED_FIELDS = ['username']  

       def __str__(self):
              return self.email

      
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=11, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.user.username} Profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()