# Generated by Django 4.0 on 2022-07-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_alter_location_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerlocationjobinterval',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
    ]
