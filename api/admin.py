from django.contrib import admin

from .models import BuddyInformation, CustomUser, GreetingMessage, SmartPoll, UnknownMessage


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "line_id"]


@admin.register(SmartPoll)
class SmartPollAdmin(admin.ModelAdmin):
    list_display = ["id", "default_name"]


@admin.register(BuddyInformation)
class BuddyInformationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "smart_poll"]


@admin.register(UnknownMessage)
class UnknownMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


@admin.register(GreetingMessage)
class GreetingMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]
