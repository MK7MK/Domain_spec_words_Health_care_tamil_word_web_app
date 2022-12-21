# Generated by Django 4.1.3 on 2022-12-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_remove_organwise_img_organwise_img_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="news",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="title", max_length=200)),
                ("tag", models.CharField(default="keyword", max_length=20)),
                ("art_link", models.URLField()),
                ("img_link", models.URLField()),
                ("desc", models.TextField(max_length=500)),
            ],
        ),
    ]
