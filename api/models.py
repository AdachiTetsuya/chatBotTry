from django.db import models


class CustomUser(models.Model):
    username = models.CharField("ユーザー名", max_length=50, blank=True, null=True)
    line_id = models.CharField("LINE ID", max_length=30, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Line アカウント"


class SmartPoll(models.Model):
    default_name = models.CharField("ポール名", max_length=30)

    class Meta:
        verbose_name_plural = "スマートポール"


class buddyInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="buddy_information")
    smart_poll = models.ForeignKey(SmartPoll, on_delete=models.CASCADE, related_name="user")

    class Meta:
        verbose_name_plural = "バディー情報"


class UnknownMessage(models.Model):
    text = models.TextField()


class GreetingMessage(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = "あいさつメッセージ"
