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

    class Meta:
        verbose_name_plural = "スマートポール"


class BuddyInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="buddy_information")
    smart_poll = models.ForeignKey(SmartPoll, on_delete=models.CASCADE, related_name="user")
    buddy_name = models.CharField("バディーネーム", max_length=50, default="")
    buddy_sage = models.IntegerField(
        "バディーの年齢", default=20, validators=[MinValueValidator(0), MaxValueValidator(130)]
    )

    def save(self, *args, **kwargs):
        if not self.buddy_name:
            self.buddy_name = self.smart_poll.default_name
        super(BuddyInformation, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "バディー情報"


class UnknownMessage(models.Model):
    text = models.TextField()


class GreetingMessage(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = "あいさつメッセージ"
