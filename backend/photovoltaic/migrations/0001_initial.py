# Generated by Django 4.1 on 2022-08-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PVData",
            fields=[
                ("timestamp", models.DateTimeField(primary_key=True, serialize=False)),
                ("irradiation", models.FloatField(default=0)),
                ("temperature_pv", models.FloatField(default=0)),
                ("temperature_amb", models.FloatField(default=0)),
                ("voltage_s1", models.FloatField(default=0)),
                ("current_s1", models.FloatField(default=0)),
                ("power_s1", models.FloatField(default=0)),
                ("voltage_s2", models.FloatField(default=0)),
                ("current_s2", models.FloatField(default=0)),
                ("power_s2", models.FloatField(default=0)),
                ("power_avg", models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]