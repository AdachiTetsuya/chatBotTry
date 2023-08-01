from django.contrib import admin

from .models import (
    BroadCastMessage,
    CustomUser,
    GreetingMessage,
    ResponseMessage,
    SmartPoll,
    UnknownMessage,
    UserPollCommentCount,
    UserPollRelation,
    UserSequence,
)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "line_id"]


@admin.register(SmartPoll)
class SmartPollAdmin(admin.ModelAdmin):
    list_display = ["id", "default_name"]


@admin.register(UserPollRelation)
class UserPollRelationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "smart_poll",
        "poll_name",
        "poll_age",
        "is_buddy",
        "relationship_level",
    ]


@admin.register(UserPollCommentCount)
class UserPollCommentCountAdmin(admin.ModelAdmin):
    list_display = ["id", "user_poll_relation", "total", "count_in_level", "updated_at"]


@admin.register(UserSequence)
class UserSequenceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "target",
        "is_change_name",
        "is_change_poll_age",
        "is_change_poll_gender",
    ]


@admin.register(UnknownMessage)
class UnknownMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


@admin.register(GreetingMessage)
class GreetingMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


@admin.register(ResponseMessage)
class ResponseMessageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "text",
        "relationship_level_min",
        "relationship_level_max",
        "poll_gender",
        "poll_age_min",
        "poll_age_max",
    ]


@admin.register(BroadCastMessage)
class BroadCastMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "on_publish", "updated_at"]
