from django.contrib import admin
from .models import UserExtension

# Register your models here.
@admin.register(UserExtension)
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'user_type')