from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('topic', 'question_text', 'pub_date', 'hits')
    list_filter = ['pub_date']
    search_fields = ['topic']
    fieldsets = [
        (None, {'fields': ['topic', 'question_text', 'author', 'hits']}),
        ('Date Information', {'fields': ['pub_date',], 'classes': ['collapse']}),
    ]

admin.site.register(Question, QuestionAdmin)