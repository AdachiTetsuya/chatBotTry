# Generated by Django 4.2.1 on 2023-06-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0011_smartpoll_can_sky_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="BroadCastMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("text", models.TextField()),
                ("on_publish", models.BooleanField(default=False, verbose_name="公開する")),
            ],
            options={
                "verbose_name_plural": "一斉送信メッセージ",
            },
        ),
    ]
