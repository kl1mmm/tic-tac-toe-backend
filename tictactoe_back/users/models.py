from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic_name = models.CharField(("patronymic"), max_length=150, blank=True)
    birth_date = models.DateField(("birthday"), null=False, blank=False)
    sex = models.CharField(("user sex"), max_length=1, blank=False)
    edited_date = models.DateTimeField(("date edited"), default=timezone.now, null=False, blank=False)
