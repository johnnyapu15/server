from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tournament)
admin.site.register(Award)
admin.site.register(Team)
admin.site.register(Team_Tournament)
admin.site.register(Summoner)
admin.site.register(Producer)
admin.site.register(Match)