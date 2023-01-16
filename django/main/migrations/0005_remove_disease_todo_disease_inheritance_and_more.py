# Generated by Django 4.1.3 on 2022-12-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_disease_casuedby_alter_disease_symptoms"),
    ]

    operations = [
        migrations.RemoveField(model_name="disease", name="todo",),
        migrations.AddField(
            model_name="disease",
            name="inheritance",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="disease",
            name="symptoms1",
            field=models.TextField(default="symp", max_length=1000),
        ),
        migrations.AddField(
            model_name="disease",
            name="symptoms2",
            field=models.TextField(default="symp", max_length=1000),
        ),
        migrations.AddField(
            model_name="disease",
            name="symptoms3",
            field=models.TextField(default="symp", max_length=1000),
        ),
        migrations.AddField(
            model_name="disease",
            name="symptoms4",
            field=models.TextField(default="symp", max_length=1000),
        ),
    ]
