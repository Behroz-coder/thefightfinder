# Generated by Django 4.0 on 2022-01-02 09:51

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_upload_player_img_player_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='img',
            field=models.ImageField(upload_to=events.models.unique_upload),
        ),
    ]