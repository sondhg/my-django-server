# Generated by Django 5.1.1 on 2024-10-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_draft', '0002_rename_ordersdraft_orderdraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdraft',
            name='end_point',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='orderdraft',
            name='order_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='orderdraft',
            name='start_point',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='orderdraft',
            name='start_time',
            field=models.CharField(max_length=8),
        ),
    ]
