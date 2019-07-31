# Generated by Django 2.1.1 on 2019-02-28 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交日期')),
                ('b_user', models.CharField(max_length=30, null=True, verbose_name='提交人')),
                ('b_type', models.CharField(max_length=100, null=True, verbose_name='Bug类型')),
                ('b_result', models.CharField(max_length=2000, null=True, verbose_name='直接结果')),
                ('b_reason', models.CharField(max_length=2000, verbose_name='原因')),
                ('b_solve', models.IntegerField(choices=[('0', '否'), ('1', '是')], default='0', verbose_name='是否解决')),
            ],
            options={
                'verbose_name': 'BugProfile',
                'db_table': 'bug',
            },
        ),
    ]