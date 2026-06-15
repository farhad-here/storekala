from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Store(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name='Store')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Owner',related_name='stores')
    description = models.TextField(blank=True,null=True,verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Last Update')
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        ordering = ['-created_at']

    def __str__(self):
        return self.name