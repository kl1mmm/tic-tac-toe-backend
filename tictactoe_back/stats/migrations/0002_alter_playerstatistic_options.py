# Generated by Django 4.2 on 2023-04-12 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="playerstatistic",
            options={
                "verbose_name": ("Статистика",),
                "verbose_name_plural": "Статистика",
            },
        ),
    ]
