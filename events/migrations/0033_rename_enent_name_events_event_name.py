# Generated by Django 4.0 on 2022-02-19 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0032_alter_events_competition_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='enent_name',
            new_name='event_name',
        ),
    ]
