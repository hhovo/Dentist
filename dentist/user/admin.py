from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_active')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('role', 'is_active')
