# Generated by Django 4.0 on 2022-01-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_player_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='upload',
            new_name='img',
        ),
        migrations.AddField(
            model_name='player',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='specification',
            field=models.TextField(blank=True),
        ),
    ]
