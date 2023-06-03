from django.contrib import admin
from leads.models import Lead
# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name","mobile_number","email","diposition","remark","status","follow_up_date")

admin.site.register(Lead,LeadAdmin)
