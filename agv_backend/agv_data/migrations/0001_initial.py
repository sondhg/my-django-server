# Generated by Django 5.1.1 on 2024-11-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGVData',
            fields=[
                ('agv_id', models.IntegerField(primary_key=True, serialize=False)),
                ('max_battery', models.IntegerField()),
                ('max_speed', models.FloatField()),
                ('max_load', models.IntegerField()),
                ('guidance_type', models.CharField(max_length=100)),
                ('is_connected', models.BooleanField(default=False)),
                ('is_busy', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
