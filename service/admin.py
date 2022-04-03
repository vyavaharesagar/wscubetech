from django.contrib import admin

# Register your models here.
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_desc','service_title','service_img')

admin.site.register(Service,ServiceAdmin)

