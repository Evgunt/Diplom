# Generated by Django 4.1.5 on 2023-02-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_docsfile_date_alter_docsfile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsfile',
            name='docs',
            field=models.FileField(blank=True, default='', upload_to='docs', verbose_name='Документ'),
        ),
    ]