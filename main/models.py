from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AdvUser(AbstractUser):
    phone = models.CharField(default="", max_length=300, verbose_name='Телефон', blank=True)
    midl_name = models.CharField(default="", max_length=300, verbose_name='Отчество', blank=True)
    dateBorn = models.CharField(default="", max_length=300, verbose_name='Дата рождения', blank=True)
    job = models.CharField(default="", max_length=300, verbose_name='Должность', blank=True)

    class Meta(AbstractUser.Meta):
        pass
