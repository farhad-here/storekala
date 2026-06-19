from django.contrib import admin
from .models import *


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name","owner","description","is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    fieldsets = (("Basic information",{"fields":("name","owner","description")}),)

# admin.site.register(Store,StoreAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock","is_active")
    list_editable = ("price","stock","is_active")
    list_filter = ("is_active",)


# admin.site.register(Product)