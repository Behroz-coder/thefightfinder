# Generated by Django 4.0 on 2022-01-02 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_event_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='reviews',
        ),
    ]
