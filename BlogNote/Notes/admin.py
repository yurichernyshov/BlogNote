from django.contrib import admin

from BlogNote.Notes.models import model_Note


@admin.register(model_Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish']
    list_filter = ['author']
