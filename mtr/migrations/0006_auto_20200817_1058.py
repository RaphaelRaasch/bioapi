# Generated by Django 2.2.5 on 2020-08-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtr', '0005_auto_20200728_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtr',
            name='id',
        ),
        migrations.AlterField(
            model_name='mtr',
            name='numero',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero'),
        ),
    ]
