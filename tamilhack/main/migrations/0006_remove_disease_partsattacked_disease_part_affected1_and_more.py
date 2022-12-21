# Generated by Django 4.1.3 on 2022-12-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_remove_disease_todo_disease_inheritance_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="disease", name="partsattacked",),
        migrations.AddField(
            model_name="disease",
            name="part_affected1",
            field=models.CharField(default="whole body", max_length=50),
        ),
        migrations.AddField(
            model_name="disease",
            name="part_affected2",
            field=models.CharField(default="whole body", max_length=50),
        ),
        migrations.AddField(
            model_name="disease",
            name="part_affected3",
            field=models.CharField(default="whole body", max_length=50),
        ),
        migrations.AddField(
            model_name="disease",
            name="part_affected4",
            field=models.CharField(default="whole body", max_length=50),
        ),
    ]
