# Generated by Django 4.0.1 on 2022-04-05 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_delete_followersreplay'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userCommunication',
        ),
    ]