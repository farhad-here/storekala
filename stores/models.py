from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


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


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
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
    
# customer panel

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} — {self.user.phone}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

    def subtotal(self):
        return self.price * self.quantity