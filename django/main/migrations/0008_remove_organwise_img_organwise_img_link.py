# Generated by Django 4.1.3 on 2022-12-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_organwise"),
    ]

    operations = [
        migrations.RemoveField(model_name="organwise", name="img",),
        migrations.AddField(
            model_name="organwise",
            name="img_link",
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
