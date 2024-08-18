from django.contrib import admin
from .models import Sadaka, DeletionLog

class SadakaAdmin(admin.ModelAdmin):
    list_display = ('date', 'day', 'sadaka1', 'shukrani')
    list_filter = ('date', 'day', 'sadaka1', 'shukrani')
    exclude = ('day',)
admin.site.register(Sadaka, SadakaAdmin)

class DeletionLogAdmin(admin.ModelAdmin):
    list_display = ('deleted_by', 'deletion_timestamp', 'sadaka1', 'shukrani','date')
    list_filter = ('deleted_by', 'deletion_timestamp', 'sadaka1', 'shukrani','date')
admin.site.register(DeletionLog, DeletionLogAdmin)
