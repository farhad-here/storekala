from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['last_name','phone', 'is_seller', 'is_staff', 'is_active']
    list_filter = ['is_seller', 'is_staff', 'is_active']
    list_editable = ['is_seller', 'is_staff', 'is_active']
    search_fields = ['phone','last_name']
    ordering = ['-created_at']


    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','phone', 'password1', 'password2', 'is_seller', 'is_staff', 'is_active'),
        }),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields = ['user__last_name', 'user__phone']