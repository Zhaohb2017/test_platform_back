# Generated by Django 2.1.1 on 2019-04-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_casesprofile_c_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casesprofile',
            name='c_status',
            field=models.IntegerField(default=0, null=True, verbose_name='用例运行状态'),
        ),
    ]
