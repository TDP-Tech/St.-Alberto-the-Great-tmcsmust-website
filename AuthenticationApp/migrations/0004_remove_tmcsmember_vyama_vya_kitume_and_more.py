# Generated by Django 4.2.11 on 2024-05-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0003_association_remove_tmcsmember_vyama_vya_kitume_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmcsmember',
            name='vyama_vya_kitume',
        ),
        migrations.DeleteModel(
            name='Association',
        ),
        migrations.AddField(
            model_name='tmcsmember',
            name='vyama_vya_kitume',
            field=models.CharField(blank=True, choices=[('LEGIO MARIA', 'LEGIO MARIA'), ('KARISMATIKI', 'KARISMATIKI'), ('KWAYA', 'KWAYA'), ('MOYO MTAKATIFU WA YESU', 'MOYO MTAKATIFU WA YESU'), ('WATUMISHI WA ALTARE', 'WATUMISHI WA ALTARE'), ('WASOMA MASOMO', 'CHAMA CHA WASOMA MASOMO')], max_length=100, verbose_name='Utume'),
        ),
    ]
