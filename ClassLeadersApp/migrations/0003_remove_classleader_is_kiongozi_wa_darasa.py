# Generated by Django 4.2.11 on 2024-05-02 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClassLeadersApp', '0002_classleader_is_kiongozi_wa_darasa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classleader',
            name='is_kiongozi_wa_darasa',
        ),
    ]