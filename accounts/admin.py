from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_seller', 'is_staff', 'is_active']
    list_filter = ['is_seller', 'is_staff', 'is_active']
    list_editable = ['is_seller', 'is_staff', 'is_active']  # ← مستقیم از لیست تغییر بده
    search_fields = ['email', 'username']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_seller', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_seller', 'is_staff', 'is_active'),
        }),
    )

    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'balance']
    search_fields = ['user__email', 'user__username']