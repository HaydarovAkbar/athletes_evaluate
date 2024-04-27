from django.contrib import admin

from .models import Ring, Match, MatchResult, Competition

admin.site.register(Ring)
admin.site.register(Match)
admin.site.register(MatchResult)
admin.site.register(Competition)