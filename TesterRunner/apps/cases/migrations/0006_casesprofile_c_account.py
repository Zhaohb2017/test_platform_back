# Generated by Django 2.1.1 on 2019-07-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20190426_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='casesprofile',
            name='c_account',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='用户mid'),
        ),
    ]
