# Generated by Django 4.0 on 2022-02-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0002_seminar_seminar_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='seminar_date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
