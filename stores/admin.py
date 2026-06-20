from django.contrib import admin
from .models import Store, Product, Order, OrderItem, Category
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "description", "is_active",)
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ['name', 'owner__email']
    list_filter = ['created_at']
    fieldsets = (("Basic information",{"fields":("name","owner","description")}),)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'store', "price", "stock", "is_active",)
    list_editable = ("price","stock","is_active",)
    search_fields = ['name', 'store__name']
    list_filter = ('store', "is_active",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__email']
    list_editable = ['status']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
