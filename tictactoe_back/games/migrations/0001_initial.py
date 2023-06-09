# Generated by Django 4.2 on 2023-04-12 08:04

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "edited_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Дата"
                    ),
                ),
                (
                    "game_timing",
                    models.CharField(default="00:00", max_length=5, verbose_name="Пол"),
                ),
                (
                    "winner",
                    models.CharField(
                        choices=[("O", "Zero"), ("X", "Cross")],
                        default="Cross",
                        max_length=5,
                        verbose_name="Победитель",
                    ),
                ),
                (
                    "player1",
                    models.ForeignKey(
                        on_delete=models.SET("Аноним А.А."),
                        related_name="player1",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "player2",
                    models.ForeignKey(
                        on_delete=models.SET("Аноним А.А."),
                        related_name="player2",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": ("Игра",), "verbose_name_plural": "История игр",},
        ),
    ]
