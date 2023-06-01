from django.urls import path

from .views import LineBotApiView

urlpatterns = [
    path("webhook/", LineBotApiView.as_view(), name="linebot-webhook"),
]
