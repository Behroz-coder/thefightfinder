# Generated by Django 4.0 on 2022-01-14 16:45

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_player_review_page_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]