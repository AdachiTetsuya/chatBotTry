from django.core.validators import MaxValueValidator, MinValueValidator
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

    def __str__(self):
        return self.default_name

    def get_temperature(self):
        "温度を返す"
        import random

        k = random.uniform(-1, 1)
        temperature = round(30 * k, 1)
        return temperature

    class Meta:
        verbose_name_plural = "スマートポール"


class UserPollRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="poll_relation")
    smart_poll = models.ForeignKey(
        SmartPoll, on_delete=models.CASCADE, related_name="user_relation"
    )
    poll_name = models.CharField("ポールの名前", max_length=50, blank=True)
    poll_age = models.IntegerField(
        "ポールの年齢", default=20, validators=[MinValueValidator(0), MaxValueValidator(130)]
    )

    def save(self, *args, **kwargs):
        if not self.poll_name:
            self.poll_name = self.smart_poll.default_name
        super(UserPollRelation, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "ユーザとポールの関係"


class UnknownMessage(models.Model):
    text = models.TextField()


class GreetingMessage(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = "あいさつメッセージ"
