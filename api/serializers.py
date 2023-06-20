from rest_framework import serializers

from .models import CustomUser, ResponseMessage


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "line_id")


class ResponseMessageListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [ResponseMessage(**attrs) for attrs in validated_data]
        ResponseMessage.objects.bulk_create(result)
        return result


class ResponseMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseMessage
        fields = (
            "text",
            "relationship_level_min",
            "relationship_level_max",
            "poll_gender",
            "poll_age_min",
            "poll_age_max",
        )
        list_serializer_class = ResponseMessageListSerializer
