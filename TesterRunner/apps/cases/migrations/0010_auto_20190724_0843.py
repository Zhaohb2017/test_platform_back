# Generated by Django 2.1.1 on 2019-07-24 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0009_auto_20190724_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casesprofile',
            name='c_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 8, 43, 16, 892611, tzinfo=utc), verbose_name='提交日期'),
        ),
    ]
