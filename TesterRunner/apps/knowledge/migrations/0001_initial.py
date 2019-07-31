# Generated by Django 2.1.1 on 2019-07-24 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_link', models.CharField(max_length=1000, verbose_name='链接')),
                ('t_title', models.CharField(max_length=1000, verbose_name='说明')),
            ],
        ),
        migrations.CreateModel(
            name='TestPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_version', models.CharField(max_length=100, null=True, verbose_name='版本')),
                ('t_module', models.CharField(default='0', max_length=100, verbose_name='模块')),
                ('t_content', models.CharField(max_length=1000, verbose_name='内容')),
                ('t_user', models.CharField(max_length=10, verbose_name='创建姓名')),
                ('t_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('t_storage', models.IntegerField(default='0', verbose_name='是否入库')),
                ('t_usable', models.IntegerField(default='0', verbose_name='是否失效')),
                ('t_img', models.ImageField(upload_to='../../static/img/%Y%M')),
                ('t_remark', models.CharField(max_length=1000, verbose_name='影响范围')),
            ],
        ),
    ]
