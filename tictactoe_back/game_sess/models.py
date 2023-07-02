from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Session(models.Model):
    """Модель сессии"""
    player1 = models.ForeignKey(User,
                                null=False,
                                blank=False,
                                on_delete=models.SET(2),
                                related_name="firstPlayer")
    player2 = models.ForeignKey(User,
                                null=False,
                                blank=False,
                                on_delete=models.SET(2),
                                related_name="secondPlayer")
    date = models.DateField(("Дата создания"), default=timezone.now, null=False, blank=False)

    class Meta:
        verbose_name = "Сессия",
        verbose_name_plural = "Активные сессии"


class Chat(models.Model):
    """Модель чата"""
    room = models.ForeignKey(Session, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Отправитель", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
