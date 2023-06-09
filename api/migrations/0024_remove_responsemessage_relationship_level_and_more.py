# Generated by Django 4.2.1 on 2023-06-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0023_remove_responsemessage_poll_generation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="responsemessage",
            name="relationship_level",
        ),
        migrations.AddField(
            model_name="responsemessage",
            name="relationship_level_max",
            field=models.IntegerField(default=5, verbose_name="仲の良さの最大値"),
        ),
        migrations.AddField(
            model_name="responsemessage",
            name="relationship_level_min",
            field=models.IntegerField(default=1, verbose_name="仲の良さの最小値"),
        ),
    ]
