# Generated by Django 4.2.1 on 2023-06-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0025_alter_responsemessage_poll_gender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersequence",
            name="is_change_poll_name",
        ),
        migrations.RemoveField(
            model_name="usersequence",
            name="is_change_user_name",
        ),
        migrations.AddField(
            model_name="usersequence",
            name="is_change_name",
            field=models.BooleanField(default=False, verbose_name="名前を変更中か"),
        ),
    ]
