# Generated by Django 4.2.1 on 2023-06-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_broadcastmessage_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResponseMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("text", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "呼ばれたときのメッセージ",
            },
        ),
        migrations.AlterField(
            model_name="greetingmessage",
            name="text",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="unknownmessage",
            name="text",
            field=models.CharField(max_length=200),
        ),
    ]