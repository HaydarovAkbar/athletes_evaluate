from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'email', 'phone_number', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('-date_joined',)
    # paginator = 10


admin.site.register(User, UserAdmin)