from django.contrib import admin
from .models import Community, Rozary, Novena, SaintLife, CommitteeMember, Image, MaswalinaMajibu, MasomoyaDominika, NewsItem, Quote, Event, CalenderYaTMCSTawiPDF, Feedback, ContactMessage, LeadersTeamMember

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('community_name', 'description', 'community_image')
    
@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'jina_la_kiongozi', 'nafasi_ya_uongozi', 'picha_ya_kiongozi','kozi_anayosoma','phone_number')

@admin.register(Rozary)
class RozaryAdmin(admin.ModelAdmin):
    list_display = ('rozary_name', 'description', 'rozary_image')
    
@admin.register(Novena)
class NovenaAdmin(admin.ModelAdmin):
    list_display = ('novena_name', 'description', 'novena_image')
    
@admin.register(SaintLife)
class SaintLifeAdmin(admin.ModelAdmin):
    list_display = ['name_of_saint', 'birth_date', 'death_date','image']
    list_filter = ['birth_date', 'death_date']
    search_fields = ['name_of_saint']
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('user','title','image')
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(MaswalinaMajibu)
class MaswalinaMajibuAdmin(admin.ModelAdmin):
    list_display = ('swali','jibu')
    

@admin.register(MasomoyaDominika)
class MasomoyaDominikaAdmin(admin.ModelAdmin):
    list_display = ('dominika','somo_la1','somo_la2','injili')
    
@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text_quote', 'author_of_quote')
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date')
    
@admin.register(CalenderYaTMCSTawiPDF)
class CalenderYaTMCSTawiPDFAdmin(admin.ModelAdmin):
    list_display = ('pdf_title', 'pdf_file')
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'message', 'created_at')

class LeadersTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('leader_name', 'leader_position', 'level', 'start_year', 'end_year', 'contact_info')
    list_filter = ('level', 'start_year', 'end_year')

admin.site.register(LeadersTeamMember, LeadersTeamMemberAdmin)

