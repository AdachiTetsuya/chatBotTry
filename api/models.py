import random

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.constants import POLL_GENDER_LIST


class CustomUser(models.Model):
    username = models.CharField("ユーザー名", max_length=50, blank=True, null=True)
    line_id = models.CharField("LINE ID", max_length=50, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Line アカウント"


class SmartPoll(models.Model):
    default_name = models.CharField("ポール名", max_length=30)
    can_sky_photo = models.BooleanField("天空カメラの有無", default=False)

    def __str__(self):
        return self.default_name

    def get_temperature(self):
        "温度を返す"
        import random

        k = random.uniform(-0.1, 2.2)
        temperature = round(20 * k, 1)
        return temperature

    def get_sky_photo(self):
        "天空写真のURLを返す"
        url = (
            "https://chat-bot-try-bucket.s3.ap-northeast-1.amazonaws.com/ocean-gdf70d992f_1280.jpg"
        )
        return url

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
    poll_gender = models.IntegerField("ポールの性別", choices=POLL_GENDER_LIST, blank=True, null=True)

    is_buddy = models.BooleanField("バディかどうか", default=False)
    is_primary = models.BooleanField("プライマリー指定", default=False)

    def save(self, *args, **kwargs):
        if not self.poll_name:
            self.poll_name = self.smart_poll.default_name
        if not self.poll_gender:
            self.poll_gender = random.randint(1, 2)
        super(UserPollRelation, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "ユーザとポールの関係"


class UserSequence(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_sequence")
    is_change_user_name = models.BooleanField("ユーザの名前を変更中か", default=False)
    is_change_poll_name = models.BooleanField("ポールの名前を変更中か", default=False)
    is_change_poll_age = models.BooleanField("ポールの年齢を変更中か", default=False)
    is_change_poll_gender = models.BooleanField("ポールの性別を変更中か", default=False)

    class Meta:
        verbose_name_plural = "ユーザの状態"


class GreetingMessage(models.Model):
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "あいさつメッセージ"


class ResponseMessage(models.Model):
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "呼ばれたときのメッセージ"


class UnknownMessage(models.Model):
    text = models.CharField(max_length=200)


class BroadCastMessage(models.Model):
    text = models.TextField()
    on_publish = models.BooleanField("公開する", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "一斉送信メッセージ"
