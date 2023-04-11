from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user_sex = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic_name = models.CharField(("Отчество"), max_length=150, blank=True)
    birth_date = models.DateField(("Дата рождения"), null=False, blank=False)
    sex = models.CharField(("Пол"), max_length=1, choices=user_sex, blank=False)
    edited_date = models.DateTimeField(("Дата изменения профиля"), default=timezone.now, null=False, blank=False)

    class Meta:
        verbose_name = 'Профиль',
        verbose_name_plural = 'Профили'