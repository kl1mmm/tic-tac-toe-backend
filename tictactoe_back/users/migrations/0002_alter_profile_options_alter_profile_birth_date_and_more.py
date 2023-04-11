# Generated by Django 4.2 on 2023-04-11 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name": ("Профиль",), "verbose_name_plural": "Профили"},
        ),
        migrations.AlterField(
            model_name="profile",
            name="birth_date",
            field=models.DateField(verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="edited_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата изменения профиля"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="patronymic_name",
            field=models.CharField(blank=True, max_length=150, verbose_name="Отчество"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="sex",
            field=models.CharField(
                choices=[("М", "Мужской"), ("Ж", "Женский")],
                max_length=1,
                verbose_name="Пол",
            ),
        ),
    ]