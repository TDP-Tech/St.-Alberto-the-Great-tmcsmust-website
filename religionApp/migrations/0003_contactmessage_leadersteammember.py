# Generated by Django 4.2.15 on 2024-08-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religionApp', '0002_community_patron_saint'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeadersTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_name', models.CharField(max_length=100)),
                ('leader_position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team_images/')),
                ('level', models.CharField(choices=[('National Leader', 'National Leader'), ('Zonal Leader', 'Zonal Leader'), ('Branch Leader', 'Branch Leader')], max_length=50)),
                ('start_year', models.PositiveIntegerField(default=2024)),
                ('end_year', models.PositiveIntegerField(default=2024)),
                ('contact_info', models.CharField(max_length=255)),
            ],
        ),
    ]