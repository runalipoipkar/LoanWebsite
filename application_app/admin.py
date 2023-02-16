from django.contrib import admin
from .models import Family, Application, Guarantor, Business

# Register your models here.
admin.site.register(Family)

admin.site.register(Application)

admin.site.register(Guarantor)

admin.site.register(Business)

