from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PlayerStatistic(models.Model):
    count_of_games = models.IntegerField(('Кол-во игр'), null=False, blank=False)
    count_of_wins = models.IntegerField(('Побед'), null=False, blank=False)
    count_of_loses = models.IntegerField(('Поражений'), null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def percent_of_wins(self):
        return (round(self.count_of_wins / self.count_of_loses)) * 100

    class Meta:
        verbose_name = 'Статистика',
        verbose_name_plural = 'Статистика'
