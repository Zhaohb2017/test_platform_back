# Generated by Django 2.1.1 on 2019-07-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddGameCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_method', models.CharField(max_length=1000, verbose_name='游戏玩法')),
                ('c_card', models.CharField(max_length=1000, verbose_name='牌数据')),
            ],
        ),
    ]
