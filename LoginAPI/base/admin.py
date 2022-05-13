from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User


# admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_valid', 'is_staff', 'is_active', 'is_superuser')