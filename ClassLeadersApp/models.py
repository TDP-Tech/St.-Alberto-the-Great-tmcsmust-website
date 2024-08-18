from django.db import models
from AuthenticationApp.models import TmcsMember

class ViongoziWaMadarasa(models.Model):
    user = models.OneToOneField(TmcsMember, on_delete=models.CASCADE, related_name='class_leader')
    
    def __str__(self):
        return f"Class Leader: {self.user.first_name} {self.user.last_name}"
