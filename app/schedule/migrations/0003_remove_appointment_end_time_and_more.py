# Generated by Django 4.0 on 2022-07-12 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='specialist',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_time',
        ),
    ]
