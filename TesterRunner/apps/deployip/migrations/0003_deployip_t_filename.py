# Generated by Django 2.1.1 on 2019-07-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployip', '0002_auto_20190730_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployip',
            name='t_filename',
            field=models.CharField(default='', max_length=1000, verbose_name='文件名'),
            preserve_default=False,
        ),
    ]
