# Generated by Django 4.2.1 on 2023-06-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_customuser_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnknownMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("text", models.TextField()),
            ],
        ),
    ]
