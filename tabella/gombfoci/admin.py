from django.contrib import admin

# Register your models here.
from .models import Team, Match, Championship, Season, Club

admin.site.register(Team)
admin.site.register(Championship)
admin.site.register(Season)
admin.site.register(Club)

#admin.site.register(Match)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['round_number', 'home_id', 'home_score', 'guest_score', 'guest_id', 'result']