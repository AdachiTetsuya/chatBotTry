from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField("ユーザー名", max_length=50, blank=True, null=True)
    line_id = models.CharField("LINE ID", max_length=30, unique=True)

    USERNAME_FIELD = "line_id"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
