# Generated by Django 4.2.11 on 2024-05-05 18:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MipangoNaFedhaApp', '0002_matumizi_matumizieditlog_matumizideletionlog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MatumiziEditLog',
            new_name='MatumiziEditedLog',
        ),
        migrations.RenameModel(
            old_name='MauzoEditLog',
            new_name='MauzoEditedLog',
        ),
    ]