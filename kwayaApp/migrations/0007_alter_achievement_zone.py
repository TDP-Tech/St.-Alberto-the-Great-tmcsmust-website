# Generated by Django 4.2.15 on 2024-08-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwayaApp', '0006_achievement_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='zone',
            field=models.TextField(choices=[('MBEYA ZONE COMPETITION', 'MBEYA ZONE COMPETITION'), ('DODOMA ZONE COMPETITION', 'DODOMA ZONE COMPETITION'), ('MBEYA PARISH', 'MBEYA PARISH'), ('NATIONAL COMPETITION', 'NATIONAL COMPETITION')]),
        ),
    ]