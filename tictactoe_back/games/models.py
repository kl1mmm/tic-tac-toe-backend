from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    game_winner = [
        ('O', 'Zero'),
        ('X', 'Cross')
    ]

    player1 = models.ForeignKey(User,
                                null=False,
                                blank=False,
                                on_delete=models.SET('Аноним А.А.'),
                                related_name='player1')
    player2 = models.ForeignKey(User,
                                null=False,
                                blank=False,
                                on_delete=models.SET('Аноним А.А.'),
                                related_name='player2')
    edited_date = models.DateField(("Дата"), default=timezone.now, null=False, blank=False)
    game_timing = models.CharField(("Пол"), max_length=5, default='00:00', null=False, blank=False)
    winner = models.CharField(("Победитель"), max_length=5, choices=game_winner, blank=False, default='Cross')

    class Meta:
        verbose_name = 'Игра',
        verbose_name_plural = 'История игр'
