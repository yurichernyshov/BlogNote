# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from BlogNote.MainPage.models import model_Note
from django.core.paginator import Paginator

def view_NotesList(request):
    notes = model_Note.objects.all()
    t = loader.get_template("page_NotesList.html")
    c = {"notes" : notes}
    return HttpResponse(t.render(c))

def view_NoteDetails(request, y, m, d, s):
    note = model_Note.objects.get(slug=s, status='published', publish__year=y, publish__month=m, publish__day=d)
    return render(request,'page_NoteDetails.html',{'note': note})

def view_Test(request, y, m, d, s):
    note = model_Note.objects.get(publish__year=y, slug=s)
    return render(request,'page_NoteDetails.html',{'note': note})

#def view_Example(request, p_year, p_month, p_day, note):
#    note = get_object_or_404(model_Note, p_yearslug=p_slug)
#    t = loader.get_template("page_NoteDetails.html")
#    c = {"note" : note}
#    return HttpResponse(t.render(c))
