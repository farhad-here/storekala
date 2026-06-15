from django.contrib import admin
from .models import *



class StoreAdmin(admin.ModelAdmin):
    list_display = ("name","owner","description","is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    fieldsets = (("اطلاعات اصلی",{"fields":("name","owner","description")}),)

admin.site.register(Store,StoreAdmin)