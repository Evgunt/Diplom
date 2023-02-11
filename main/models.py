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


class DocsFile(models.Model):
    name = models.CharField(unique=True, max_length=300, default="", blank=False, verbose_name='Название')
    date = models.CharField(max_length=300, default="", blank=True, verbose_name='Дата добавления')
    extension = models.CharField(max_length=300, default="", blank=True, verbose_name='Расширение')
    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE, blank=False, verbose_name='Владелец',
                              to_field="username", default="")
    status = models.BooleanField(default=False, verbose_name='Публичный')
    comments = models.TextField(default="", blank=False, verbose_name='Комментарий')
    docs = models.FileField(default="", blank=True, verbose_name='Документ', upload_to='media/docs'),

    class Meta:
        verbose_name_plural = 'Документы'
        verbose_name = 'Документ'

    def __str__(self):
        return self.name
