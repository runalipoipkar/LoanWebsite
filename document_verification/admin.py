from django.contrib import admin
from .models import Bank, Document


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ['user', 'bank_name', 'current_account_no', 'ifsc_code', 'passbook_copy']
admin.site.register(Bank, BankAdmin)

admin.site.register(Document)
