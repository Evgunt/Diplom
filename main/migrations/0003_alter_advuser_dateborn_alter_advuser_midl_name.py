# Generated by Django 4.1.5 on 2023-02-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_advuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='dateBorn',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='midl_name',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Отчество'),
        ),
    ]
