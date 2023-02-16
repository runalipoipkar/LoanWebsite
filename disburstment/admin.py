from django.contrib import admin
from .models import Vendor, Installment, Disbursement

# Register your models here.
admin.site.register(Vendor)

admin.site.register(Installment)

admin.site.register(Disbursement)