from django.db import models
from AuthenticationApp.models import TmcsMember

TRANSACTION_CHOICES = (
    ('Ada', 'Ada'),
    ('Zaka', 'Zaka'),
    ('Tunisha mfuko', 'Tunisha mfuko'),
    ('Sherehe na Maafa', 'Sherehe na Maafa'),
    ('Cheti', 'Cheti'),
)

class MemberTransaction(models.Model):
    member = models.ForeignKey(TmcsMember, on_delete=models.CASCADE, related_name='transactions', verbose_name='Member Unique Identifier')
    transaction_type = models.CharField(max_length=50, verbose_name='Transaction Type', choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    transaction_date = models.DateField(auto_now_add=True, verbose_name='Transaction Date')
    created_by = models.ForeignKey(TmcsMember, on_delete=models.SET_NULL, related_name='created_transactions', verbose_name='Created By',null=True)
    
    def __str__(self):
        return f"{self.member.first_name} {self.member.middle_name} {self.member.last_name} - {self.transaction_type} - {self.transaction_date}"

    class Meta:
        verbose_name = 'Michango ya Chama'
        verbose_name_plural = 'Michango ya Chama'

