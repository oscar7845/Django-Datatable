# Generated by Django 4.0.6 on 2022-08-17 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 17, 16, 43, 42, 23152, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='note',
            field=models.TextField(default=datetime.datetime(2022, 8, 17, 16, 43, 55, 446717, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
