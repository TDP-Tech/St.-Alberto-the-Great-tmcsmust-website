from django.contrib import admin
from .models import MemberTransaction

# Register your models here.
@admin.register(MemberTransaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['member','transaction_type', 'amount', 'created_by', 'transaction_date']
    list_filter = ['created_by', 'transaction_type', 'transaction_date']
    search_fields = ('member__unique_identifier', 'transaction_type')

