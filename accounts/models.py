from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):
       def _create_user(self, phone,first_name,last_name, password=None, **extra_fields):
              if not phone:
                     raise ValueError('Inserting phone is necessary')
              if not first_name and not last_name:
                     raise ValueError('full name is necessary')

              user = self.model(phone=phone,first_name=first_name,last_name=last_name, **extra_fields)
              user.set_password(password)
              user.save(using=self._db)
              return user
       def create_user(self, phone,first_name,last_name, password=None, **extra_fields):
              extra_fields.setdefault('is_staff', False)
              extra_fields.setdefault('is_active', True)
              return self._create_user(phone, first_name,last_name, password, **extra_fields)
       
       def create_superuser(self, phone,first_name,last_name, password, **extra_fields):
              extra_fields.setdefault('is_staff', True)
              extra_fields.setdefault('is_active', True)
              extra_fields.setdefault('is_superuser', True)
              if extra_fields.get('is_active') is not True:
                     raise ValueError('superuser mush have is_active=True')
              if extra_fields.get('is_staff') is not True:
                     raise ValueError('superuser mush have is_staff=True')
              if extra_fields.get('is_superuser') is not True:
                     raise ValueError('superuser mush have is_superuser=True')

              return self._create_user(phone,first_name,last_name, password, **extra_fields)
       
  


class User(AbstractBaseUser, PermissionsMixin):
        phone = models.CharField(max_length=15, unique=True, verbose_name="Phone Number")
        first_name = models.CharField(max_length=100,verbose_name="First Name")
        last_name = models.CharField(max_length=100,verbose_name="Last Name")
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_seller = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        objects = CustomUserManager()
        USERNAME_FIELD = 'phone'        
        REQUIRED_FIELDS = ['first_name','last_name']  

        def __str__(self):
            return f"{self.first_name} {self.last_name}"
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.user.phone} Profile"
    
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()