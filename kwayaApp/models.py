from django.db import models
from AuthenticationApp.models import TmcsMember

TRANSACTION_CHOICES = (
    ('Ada', 'Ada'),
)

VOICE_CHOICES = (
    ('Soprano', 'Soprano (I)'),
    ('Alto', 'Alto (II)'),
    ('Tenor', 'Tenor (III)'),
    ('Bass', 'Bass (IV)'),
)

TALENT_CHOICES = (
    ('Mpiga Kinanda', 'Mpiga Kinanda'),
    ('Mwalimu wa Nota', 'Mwalimu wa Nota'),
    ('Mpiga Ngoma', 'Mpiga Ngoma'),
    ('Gitaa', 'Gitaa'),
)


class Video(models.Model):
    title = models.CharField(max_length=100)
    embed_code = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class KwayaMemberTransaction(models.Model):
    member = models.ForeignKey(TmcsMember, on_delete=models.CASCADE, related_name='kwayaTransactions', verbose_name='Member Unique Identifier')
    transaction_type = models.CharField(max_length=50, verbose_name='Transaction Type', choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    transaction_date = models.DateField(auto_now_add=True, verbose_name='Transaction Date')

    def __str__(self):
        return f"{self.member.first_name} {self.member.middle_name} {self.member.last_name} - {self.transaction_type} - {self.transaction_date}"

    class Meta:
        verbose_name = 'Kwaya Malipo ya Ada'
        verbose_name_plural = 'Kwaya Malipo ya Ada'


class KwayaVoiceAssignment(models.Model):
    member = models.OneToOneField(TmcsMember, on_delete=models.CASCADE, related_name='kwaya_assignment')
    voice = models.CharField(max_length=10, choices=VOICE_CHOICES)
    talent = models.CharField(max_length=20, choices=TALENT_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.voice} - {self.talent}"


# models.py

from django.db import models

class Achievement(models.Model):
    POSITION_CHOICES = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
        (6, 'Six'),
        (7, 'Seventh'),
        (8, 'Eighth'),
        (9, 'Ninth'),
        (10, 'Tenth'),
    ]
    ZONE_CHOICES = [
        ('MBEYA ZONE COMPETITION', 'MBEYA ZONE COMPETITION'),
        ('DODOMA ZONE COMPETITION', 'DODOMA ZONE COMPETITION'),
        ('MBEYA PARISH', 'MBEYA PARISH'),
        ('NATIONAL COMPETITION', 'NATIONAL COMPETITION'),
    ]
    
    winner_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    position_winning = models.IntegerField(choices=POSITION_CHOICES)
    zone = models.TextField(choices=ZONE_CHOICES)
    year = models.IntegerField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"
