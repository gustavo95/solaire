# Generated by Django 3.2 on 2022-08-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photovoltaic', '0013_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='days_left',
            field=models.IntegerField(default=7),
        ),
    ]
