# Generated by Django 2.2.5 on 2020-07-06 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtr', '0002_mtr_motorista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtr',
            name='cliente',
        ),
    ]
