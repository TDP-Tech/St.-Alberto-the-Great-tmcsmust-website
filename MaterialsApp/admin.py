from django.contrib import admin
from .models import StudyMaterial

# Define a custom admin class for the Material model
class MaterialAdmin(admin.ModelAdmin):
    # Display these fields in the change list
    list_display = ('course','title', 'level','year_of_study', 'date_posted')

    # Add filters for level
    list_filter = ('level',)

# Register your models with the custom admin class
admin.site.register(StudyMaterial, MaterialAdmin)
