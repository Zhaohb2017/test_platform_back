# Generated by Django 2.1.1 on 2019-10-16 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testReport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekly',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weekly',
            name='date',
            field=models.DateField(default=''),
        ),
    ]
