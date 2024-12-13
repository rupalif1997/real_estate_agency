from django.contrib import admin
from .models import listings
from properties.models import Msg
# Register your models here.
# class AgentAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'contact', 'email', 'experience')
#     search_fields = ('full_name', 'contact', 'email')
    
# admin.site.register(Agent, AgentAdmin)   
admin.site.register(Msg)
admin.site.register(listings)
# admin.site.register(Payment_tb)