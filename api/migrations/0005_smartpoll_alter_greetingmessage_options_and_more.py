# Generated by Django 4.2.1 on 2023-06-02 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_greetingmessage"),
    ]

    operations = [
        migrations.CreateModel(
            name="SmartPoll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("default_name", models.CharField(max_length=30, verbose_name="ポール名")),
            ],
            options={
                "verbose_name_plural": "スマートポール",
            },
        ),
        migrations.AlterModelOptions(
            name="greetingmessage",
            options={"verbose_name_plural": "あいさつメッセージ"},
        ),
        migrations.CreateModel(
            name="buddyInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "smart_poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to="api.smartpoll",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buddy_information",
                        to="api.customuser",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "バディー情報",
            },
        ),
    ]
