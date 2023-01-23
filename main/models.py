from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AdvUser(AbstractUser):
    phone = models.CharField(default="", max_length=300, verbose_name='Телефон')
    key = models.CharField(default="", max_length=300)

    class Meta(AbstractUser.Meta):
        pass
