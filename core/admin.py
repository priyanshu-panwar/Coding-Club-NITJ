from django.contrib import admin
from .models import Contact, TeamMember, Event

admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(TeamMember)