# Generated by Django 4.2.1 on 2023-06-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0010_alter_customuser_line_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="smartpoll",
            name="can_sky_photo",
            field=models.BooleanField(default=False, verbose_name="天空カメラの有無"),
        ),
    ]
