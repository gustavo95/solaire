# Generated by Django 3.2 on 2022-08-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photovoltaic', '0010_alerttreshold_yieldminute'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvstring',
            name='string_number',
            field=models.IntegerField(default=0),
        ),
    ]
