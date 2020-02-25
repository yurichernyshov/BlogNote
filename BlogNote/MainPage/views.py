# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from BlogNote.MainPage.models import model_MainPage

def view_MainPage(request):
    notes = model_MainPage.objects.all()
    t = loader.get_template("page_MainPage.html")
    c = {"notes" : notes}
    return HttpResponse(t.render(c))
