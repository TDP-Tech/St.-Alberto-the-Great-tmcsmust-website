from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'displayname', 'carrier']
    search_fields = ['user__username', 'displayname']
    list_filter = ['user__is_active']

admin.site.register(Profile, ProfileAdmin)
