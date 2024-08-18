from django.contrib import admin
from .models import Video, KwayaMemberTransaction, KwayaVoiceAssignment, Achievement
# Register your models here.
admin.site.register(Video)

class KwayaVoiceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('member', 'voice', 'talent')
    list_filter = ('voice', 'talent')
admin.site.register(KwayaVoiceAssignment, KwayaVoiceAssignmentAdmin)


@admin.register(KwayaMemberTransaction)
class KwayaMemberTransactionAdmin(admin.ModelAdmin):
    list_display = ['member','transaction_type', 'amount', 'transaction_date']
    list_filter = ['transaction_type', 'transaction_date']
    search_fields = ('member__unique_identifier', 'transaction_type')
    
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('winner_name','zone','title', 'year', 'position_winning')
    search_fields = ('title', 'year', 'position')