# Generated by Django 4.1.5 on 2023-02-12 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_docsfile_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsfile',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
    ]
