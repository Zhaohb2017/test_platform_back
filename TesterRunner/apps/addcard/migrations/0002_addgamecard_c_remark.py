# Generated by Django 2.1.1 on 2019-07-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addgamecard',
            name='c_remark',
            field=models.CharField(default='', max_length=1000, verbose_name='备注'),
            preserve_default=False,
        ),
    ]
