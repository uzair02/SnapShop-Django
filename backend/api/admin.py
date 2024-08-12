from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.models import User, Profile

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'bio', 'image', 'verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)