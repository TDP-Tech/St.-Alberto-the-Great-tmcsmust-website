# Generated by Django 4.2.11 on 2024-05-03 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kwayaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KwayaVoiceAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice', models.CharField(choices=[('Soprano', 'Soprano'), ('Alto', 'Alto'), ('Tenor', 'Tenor'), ('Bass', 'Bass')], max_length=10)),
                ('talent', models.CharField(choices=[('Mpiga Kinanda', 'Mpiga Kinanda'), ('Mwalimu wa Nota', 'Mwalimu wa Nota'), ('Mpiga Ngoma', 'Mpiga Ngoma'), ('Gitaa', 'Gitaa')], max_length=20)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kwaya_assignment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]