# Generated by Django 2.1.7 on 2020-11-27 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201127_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 27, 17, 11, 30, 852629)),
        ),
    ]
