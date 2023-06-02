from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser, GreetingMessage, UnknownMessage


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "line_id"]
    list_filter = []
    ordering = []
    filter_horizontal = []
    fieldsets = (
        (
            None,
            {"fields": ()},
        ),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )


@admin.register(UnknownMessage)
class UnknownMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


@admin.register(GreetingMessage)
class GreetingMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]
