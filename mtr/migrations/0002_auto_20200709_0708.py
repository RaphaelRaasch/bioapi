# Generated by Django 2.2.5 on 2020-07-09 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mtr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtr',
            name='cliente',
        ),
        migrations.AddField(
            model_name='mtr',
            name='motorista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]