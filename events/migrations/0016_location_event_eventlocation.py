# Generated by Django 4.0 on 2022-01-06 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_player_competition_level_player_competition_style_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=10)),
                ('lng', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='eventLocation',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.location'),
            preserve_default=False,
        ),
    ]