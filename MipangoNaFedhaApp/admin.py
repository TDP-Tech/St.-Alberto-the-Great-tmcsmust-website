from django.contrib import admin
from .models import Mauzo, MauzoDeletionLog, MauzoEditedLog, Matumizi, MatumiziDeletionLog, MatumiziEditedLog

class MauzoAdmin(admin.ModelAdmin):
    list_display = ('date', 'day', 'mauzo_tshirt', 'mauzo_visakramenti', 'mauzo_vipeperushi', 'mapato_saloon')
    list_filter = ('date', 'day')

class MauzoDeletionLogAdmin(admin.ModelAdmin):
    list_display = ('deleted_by', 'deletion_timestamp', 'date', 'mauzo_tshirt', 'mauzo_visakramenti', 'mauzo_vipeperushi', 'mapato_saloon')
    list_filter = ('deletion_timestamp', 'date')

class MauzoEditLogAdmin(admin.ModelAdmin):
    list_display = ('edited_by', 'edit_timestamp', 'mauzo', 'mauzo_tshirt_before', 'mauzo_visakramenti_before', 'mauzo_vipeperushi_before', 'mapato_saloon_before', 'mauzo_tshirt_after', 'mauzo_visakramenti_after', 'mauzo_vipeperushi_after', 'mapato_saloon_after')
    list_filter = ('edit_timestamp',)

class MatumiziAdmin(admin.ModelAdmin):
    list_display = ['date', 'matumizi_tshirt', 'matumizi_visakramenti', 'matumizi_vipeperushi', 'matumizi_saloon']
    list_filter = ['date']
    search_fields = ['date']

class MatumiziDeletionLogAdmin(admin.ModelAdmin):
    list_display = ['deleted_by', 'deletion_timestamp', 'date', 'matumizi_tshirt', 'matumizi_visakramenti', 'matumizi_vipeperushi', 'matumizi_saloon', 'reason']
    list_filter = ['deletion_timestamp']
    search_fields = ['deleted_by__first_name', 'deleted_by__last_name', 'date']

class MatumiziEditLogAdmin(admin.ModelAdmin):
    list_display = ['edited_by', 'edit_timestamp', 'matumizi', 'matumizi_tshirt_before', 'matumizi_visakramenti_before', 'matumizi_vipeperushi_before', 'matumizi_saloon_before', 'matumizi_tshirt_after', 'matumizi_visakramenti_after', 'matumizi_vipeperushi_after', 'matumizi_saloon_after']
    list_filter = ['edit_timestamp']
    search_fields = ['edited_by__first_name', 'edited_by__last_name', 'matumizi__date']

admin.site.register(Mauzo, MauzoAdmin)
admin.site.register(MauzoDeletionLog, MauzoDeletionLogAdmin)
admin.site.register(MauzoEditedLog, MauzoEditLogAdmin)
admin.site.register(Matumizi, MatumiziAdmin)
admin.site.register(MatumiziDeletionLog, MatumiziDeletionLogAdmin)
admin.site.register(MatumiziEditedLog, MatumiziEditLogAdmin)


