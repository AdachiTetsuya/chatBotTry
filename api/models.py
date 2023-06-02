from django.db import models


class CustomUser(models.Model):
    username = models.CharField("ユーザー名", max_length=50, blank=True, null=True)
    line_id = models.CharField("LINE ID", max_length=30, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Line アカウント"
