# Generated by Django 5.1.1 on 2024-10-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_draft', '0006_alter_orderdraft_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdraft',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
