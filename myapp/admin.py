from django.contrib import admin
from .models import Contact, Employee

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['full_name', 'email', 'subject']
    
# Register your models here.
admin.site.register(Employee)