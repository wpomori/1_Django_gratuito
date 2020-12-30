from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'is_activate', 'is_staff', 'date_joined')


admin.site.register(User, UserAdmin)
