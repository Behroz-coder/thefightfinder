# Generated by Django 4.0 on 2022-01-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_eventtype_event_status_alter_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
