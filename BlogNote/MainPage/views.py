# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from numpy.random import choice

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from BlogNote.MainPage.models import model_Note
from .forms import InputNoteForm, TestForm

def view_NotesList(request):
    object_list = model_Note.objects.all()
    paginator = Paginator(object_list, 3) # 3 articles on page
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        # ≈сли страница не €вл€етс€ целым числом, возвращаем первую страницу.
        notes = paginator.page(1)
    except EmptyPage:
        # ≈сли номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        notes = paginator.page(paginator.num_pages)
    return render(request,'page_NotesList.html', {'page': page, 'notes': notes})

def view_NoteDetails(request, y, m, d, s):
    note = model_Note.objects.get(slug=s, publish__year=y, publish__month=m, publish__day=d)
    return render(request,'page_NoteDetails.html',{'note': note})

def view_InputNote(request):
    note = model_Note()

    saved = False
    if request.method == 'POST':
        form = InputNoteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            #save new note
            note.title=cd['title']
            note.slug = str(choice([i for i in range(1,10)])) + \
                        str(choice([i for i in range(1,10)])) + \
                        str(choice([i for i in range(1,10)])) + \
                        str(choice([i for i in range(1,10)]))
            note.body=cd['body']
            note.author=User.objects.get(username=cd['author'])
            note.status = cd['status']
#            publish = models.DateTimeField(default=timezone.now)
#            created = models.DateTimeField(auto_now_add=True)
#            updated = models.DateTimeField(auto_now=True)
            note.save()

            saved = True
            return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})
        else:
            form = InputNoteForm()
            return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})
    else:
        form = InputNoteForm()
        return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})

def view_Test(request):
    form = TestForm(initial={'id': 1})
    form.id=1
    print("form:", form.as_p())
    print("form.id:", form.id)
    return render(request, 'test.html', {'pform': form})

