# Generated by Django 4.0 on 2022-01-14 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_new_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='date',
        ),
        migrations.RemoveField(
            model_name='new',
            name='time',
        ),
    ]