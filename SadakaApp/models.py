from django.db import models
from django.conf import settings

class Sadaka(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=50, blank=True)
    sadaka1 = models.DecimalField(max_digits=17, decimal_places=2, null=True, blank=True)
    shukrani = models.DecimalField(max_digits=17, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.sadaka1 is not None and self.shukrani is None:
            self.shukrani = 0
        if self.sadaka1 is None and self.shukrani is not None:
            self.sadaka1= 0
        if self.sadaka1 is None and self.shukrani is None:
            self.sadaka1 = 0
            self.shukrani = 0
        if self.date:
            # Calculate day based on date if not provided
            self.day = self.date.strftime("%A")
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Sadaka'
        verbose_name_plural = 'Sadaka'


class DeletionLog(models.Model):
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    deletion_timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    sadaka1 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shukrani = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"Deleted by {self.deleted_by.first_name}  {self.deleted_by.last_name} at {self.deletion_timestamp}"
