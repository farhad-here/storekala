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


class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name="Name")
    price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name="Price")
    description = models.TextField(blank=True, null=True,verbose_name="Descriptions")
    image = models.ImageField( upload_to="stores/images/",verbose_name="Image")
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name