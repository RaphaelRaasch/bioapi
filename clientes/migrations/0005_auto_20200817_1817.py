# Generated by Django 2.2.5 on 2020-08-17 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20200817_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_multidev',
            field=models.IntegerField(verbose_name='Id Multidev'),
        ),
    ]