# Generated by Django 5.1.1 on 2024-10-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_draft', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrdersDraft',
            new_name='OrderDraft',
        ),
    ]