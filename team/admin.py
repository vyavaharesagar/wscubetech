from django.contrib import admin

# Register your models here.
from team.models import Team

class TeamAdmin(admin.ModelAdmin):
    displayContent = ('name','designation','profile','twitter','instagram','linkedin','facebook')


admin.site.register(Team,TeamAdmin)
