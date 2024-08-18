from django.db import models
from AuthenticationApp.models import TmcsMember

TRANSACTION_CHOICES = (
    ('Ada', 'Ada'),
)

    

class LegioMemberTransaction(models.Model):
    member = models.ForeignKey(TmcsMember, on_delete=models.CASCADE, related_name='legioTransactions', verbose_name='Member Unique Identifier')
    transaction_type = models.CharField(max_length=50, verbose_name='Transaction Type', choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    transaction_date = models.DateField(auto_now_add=True, verbose_name='Transaction Date')

    def __str__(self):
        return f"{self.member.first_name} {self.member.middle_name} {self.member.last_name} - {self.transaction_type} - {self.transaction_date}"

    class Meta:
        verbose_name = 'Legio Malipo ya Ada'
        verbose_name_plural = 'Legio Malipo ya Ada'

