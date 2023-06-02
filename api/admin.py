from django.contrib import admin

from .models import CustomUser, GreetingMessage, SmartPoll, UnknownMessage, UserPollRelation


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "line_id"]


@admin.register(SmartPoll)
class SmartPollAdmin(admin.ModelAdmin):
    list_display = ["id", "default_name"]


@admin.register(UserPollRelation)
class UserPollRelationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "smart_poll", "poll_name", "poll_age"]


@admin.register(UnknownMessage)
class UnknownMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


@admin.register(GreetingMessage)
class GreetingMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]
