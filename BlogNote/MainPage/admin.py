# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from BlogNote.MainPage.models import model_Note

admin.site.register(model_Note)

class model_NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

