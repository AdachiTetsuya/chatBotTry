# Generated by Django 4.2.1 on 2023-06-17 14:19

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0018_alter_usersequence_options_usersequence_target"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userpollrelation",
            name="relationship_level",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="仲の良さ",
            ),
        ),
        migrations.CreateModel(
            name="UserPollCommentCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "user_comment_count",
                    models.IntegerField(default=0, verbose_name="ユーザから呼びかけられた回数"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user_poll_relation",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_count",
                        to="api.userpollrelation",
                    ),
                ),
            ],
        ),
    ]