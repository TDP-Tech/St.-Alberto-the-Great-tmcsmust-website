from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class Mauzo(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=50, blank=True)
    mauzo_tshirt = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)
    mauzo_visakramenti = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)
    mauzo_vipeperushi = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)
    mapato_saloon = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)

    def clean(self):
        if self.mauzo_tshirt is not None and self.mauzo_tshirt < 0:
            raise ValidationError("Amount for mauzo ya T-shirt cannot be negative.")
        if self.mauzo_visakramenti is not None and self.mauzo_visakramenti < 0:
            raise ValidationError("Amount for mauzo ya Visakramenti cannot be negative.")
        if self.mauzo_vipeperushi is not None and self.mauzo_vipeperushi < 0:
            raise ValidationError("Amount for mauzo ya Vipeperushi cannot be negative.")
        if self.mapato_saloon is not None and self.mapato_saloon < 0:
            raise ValidationError("Amount for mapato ya Saloon cannot be negative.")
    
    def save(self, *args, **kwargs):
        if self.date:
            self.day = self.date.strftime("%A")
        super().save(*args, **kwargs)
        if self.pk:  # Check if the instance is already saved in the database
            original_instance = Mauzo.objects.get(pk=self.pk)
            if self != original_instance:  # Check if any fields have changed
                MauzoEditedLog.objects.create(
                    edited_by=None,  # You might want to update this to reflect the actual user
                    mauzo=self,
                    mauzo_tshirt_before=original_instance.mauzo_tshirt,
                    mauzo_visakramenti_before=original_instance.mauzo_visakramenti,
                    mauzo_vipeperushi_before=original_instance.mauzo_vipeperushi,
                    mapato_saloon_before=original_instance.mapato_saloon,
                    mauzo_tshirt_after=self.mauzo_tshirt,
                    mauzo_visakramenti_after=self.mauzo_visakramenti,
                    mauzo_vipeperushi_after=self.mauzo_vipeperushi,
                    mapato_saloon_after=self.mapato_saloon,
                )
        
    class Meta:
        verbose_name = 'Mauzo'
        verbose_name_plural = 'Mauzo'


class MauzoDeletionLog(models.Model):
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    deletion_timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    mauzo_tshirt = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_visakramenti = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_vipeperushi = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mapato_saloon = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    reason = models.CharField(max_length=255)
    def __str__(self):
        return f"Deleted by {self.deleted_by.first_name} {self.deleted_by.last_name} at {self.deletion_timestamp}"
    

class MauzoEditedLog(models.Model):
    edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    edit_timestamp = models.DateTimeField(auto_now_add=True)
    mauzo = models.ForeignKey(Mauzo, on_delete=models.CASCADE)
    mauzo_tshirt_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_visakramenti_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_vipeperushi_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mapato_saloon_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_tshirt_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_visakramenti_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mauzo_vipeperushi_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    mapato_saloon_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)

    def __str__(self):
        return f"Edited by {self.edited_by.first_name} {self.edited_by.last_name} at {self.edit_timestamp}"
    
####################################
####################################
class Matumizi(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=50, blank=True)
    matumizi_tshirt = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)
    matumizi_visakramenti = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)
    matumizi_vipeperushi = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)
    matumizi_saloon = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True, default=0)

    def clean(self):
        if self.matumizi_tshirt is not None and self.matumizi_tshirt < 0:
            raise ValidationError("Amount for matumizi ya T-shirt cannot be negative.")
        if self.matumizi_visakramenti is not None and self.matumizi_visakramenti < 0:
            raise ValidationError("Amount for matumizi ya Visakramenti cannot be negative.")
        if self.matumizi_vipeperushi is not None and self.matumizi_vipeperushi < 0:
            raise ValidationError("Amount for matumizi ya Vipeperushi cannot be negative.")
        if self.matumizi_saloon is not None and self.matumizi_saloon < 0:
            raise ValidationError("Amount for matumizi ya Saloon cannot be negative.")

    def save(self, *args, **kwargs):
        if self.date:
            self.day = self.date.strftime("%A")
        super().save(*args, **kwargs)
        if self.pk:  # Check if the instance is already saved in the database
            original_instance = Matumizi.objects.get(pk=self.pk)
            if self != original_instance:  # Check if any fields have changed
                user = None
                MatumiziEditedLog.objects.create(
                    edited_by=user,  # You might want to update this to reflect the actual user
                    matumizi=self,
                    matumizi_tshirt_before=original_instance.matumizi_tshirt,
                    matumizi_visakramenti_before=original_instance.matumizi_visakramenti,
                    matumizi_vipeperushi_before=original_instance.matumizi_vipeperushi,
                    matumizi_saloon_before=original_instance.matumizi_saloon,
                    matumizi_tshirt_after=self.matumizi_tshirt,
                    matumizi_visakramenti_after=self.matumizi_visakramenti,
                    matumizi_vipeperushi_after=self.matumizi_vipeperushi,
                    matumizi_saloon_after=self.matumizi_saloon,
                )
        
    class Meta:
        verbose_name = 'Matumizi'
        verbose_name_plural = 'Matumizi'


class MatumiziDeletionLog(models.Model):
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    deletion_timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    matumizi_tshirt = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_visakramenti = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_vipeperushi = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_saloon = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    reason = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Deleted by {self.deleted_by.first_name} {self.deleted_by.last_name} at {self.deletion_timestamp}"
    

class MatumiziEditedLog(models.Model):
    edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    edit_timestamp = models.DateTimeField(auto_now_add=True)
    matumizi = models.ForeignKey(Matumizi, on_delete=models.CASCADE)
    matumizi_tshirt_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_visakramenti_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_vipeperushi_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_saloon_before = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_tshirt_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_visakramenti_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_vipeperushi_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    matumizi_saloon_after = models.DecimalField(max_digits=13, decimal_places=2, null=True)

    def __str__(self):
        return f"Edited by {self.edited_by.first_name} {self.edited_by.last_name} at {self.edit_timestamp}"

