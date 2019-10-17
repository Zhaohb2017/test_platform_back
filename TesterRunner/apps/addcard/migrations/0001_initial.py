# Generated by Django 2.1.1 on 2019-10-12 08:30

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
                ('c_versions', models.CharField(max_length=1000, verbose_name='版本')),
                ('c_method', models.CharField(max_length=1000, verbose_name='游戏玩法')),
                ('c_card', models.CharField(max_length=1000, verbose_name='牌数据')),
                ('c_remark', models.CharField(max_length=1000, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='LogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=1000, verbose_name='操作人')),
                ('info', models.CharField(max_length=1000, verbose_name='操作信息')),
            ],
        ),
    ]
