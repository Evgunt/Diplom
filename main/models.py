from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AdvUser(AbstractUser):
    phone = models.CharField(default="", max_length=300, verbose_name='Телефон')
    midl_name = models.CharField(default="", max_length=300, verbose_name='Отчество')
    dateBorn = models.CharField(default="", max_length=300, verbose_name='Дата рождения')

    class Meta(AbstractUser.Meta):
        pass
