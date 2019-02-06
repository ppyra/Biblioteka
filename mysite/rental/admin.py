from django.contrib import admin
from .models import Rental

# Register your models here.

class RentaAdmin(admin.ModelAdmin):
    search_fields = ['who', 'what', 'when']
    ordering = ['when']

admin.site.register(Rental, RentaAdmin)
