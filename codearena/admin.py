from django.contrib import admin
from .models import Coding_Profile, Event, Question, Solution

admin.site.register(Coding_Profile)
admin.site.register(Question)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'date_valid')
    list_filter = ['date_posted']
    search_fields = ['title']
    fieldsets = [
        (None, {'fields': ['title',]}),
        ('Date Information', {'fields': ['date_posted', 'date_valid'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]

admin.site.register(Event, EventAdmin)

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('coder', 'event')
    list_filter = ['event',]
    search_fields = ['event',]

admin.site.register(Solution, SolutionAdmin)