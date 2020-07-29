# Generated by Django 2.2.5 on 2020-07-29 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sequencia', '0001_initial'),
        ('mtr', '0005_auto_20200728_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='MtrItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtr.Mtr')),
                ('sequencia', models.ManyToManyField(to='sequencia.Sequencia')),
            ],
        ),
    ]
