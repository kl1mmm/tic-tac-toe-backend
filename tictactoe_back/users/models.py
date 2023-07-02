from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    class UserSex(models.TextChoices):
        male = 'М', 'Мужской'
        female = 'Ж', 'Женский'

    class UserStatus(models.TextChoices):
        on_line = 'Online', 'В сети'
        off_line = 'Offline', 'Не в сети'
        in_game = 'In Game', 'В игре'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    patronymic_name = models.CharField(("Отчество"), max_length=150, blank=True)
    birth_date = models.DateTimeField(("Дата рождения"), null=False, blank=False)
    sex = models.CharField(("Пол"), max_length=1, choices=UserSex.choices, blank=False)
    edited_date = models.DateTimeField(("Дата изменения профиля"), default=timezone.now, null=False, blank=False)
    online_status = models.CharField(("Статус"), default="Offline", max_length=7, choices=UserStatus.choices, blank=False)

    class Meta:
        verbose_name = 'Профиль',
        verbose_name_plural = 'Профили'
