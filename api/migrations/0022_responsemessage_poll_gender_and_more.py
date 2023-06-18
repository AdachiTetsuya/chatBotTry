# Generated by Django 4.2.1 on 2023-06-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0021_userpollcommentcount_continuous_day_in_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="responsemessage",
            name="poll_gender",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "男性"), (2, "女性"), (3, "その他")],
                null=True,
                verbose_name="ポールの性別",
            ),
        ),
        migrations.AddField(
            model_name="responsemessage",
            name="poll_generation",
            field=models.IntegerField(
                choices=[
                    (1, "乳児期"),
                    (2, "幼児期"),
                    (3, "学童期"),
                    (4, "青年期"),
                    (5, "成人期"),
                    (6, "壮年期"),
                    (7, "老年期"),
                ],
                default=4,
                verbose_name="ポールの発達段階",
            ),
        ),
        migrations.AddField(
            model_name="responsemessage",
            name="relationship_level",
            field=models.IntegerField(default=3, verbose_name="仲の良さ"),
        ),
    ]
