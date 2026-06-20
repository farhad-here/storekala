from django.contrib import admin
from .models import *


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


