# Generated by Django 4.1.5 on 2023-03-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_docsid_sendeddocs_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendeddocs',
            name='read',
            field=models.BooleanField(default=0),
        ),
    ]
