# Generated by Django 4.2 on 2023-04-30 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_profile_birth_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="birth_date",),
    ]