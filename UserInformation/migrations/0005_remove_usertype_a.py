# Generated by Django 4.0 on 2022-02-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserInformation', '0004_usertype_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='a',
        ),
    ]
