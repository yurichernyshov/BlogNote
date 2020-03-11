from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from BlogNote.Notes.models import model_Note
from BlogNote.Notes.forms import InputNoteForm

def view_StartPage(request):
    return render(request,'page_StartPage.html')

@login_required
def view_NotesList(request):
    object_list = model_Note.objects.all()
    paginator = Paginator(object_list, 3) # 3 articles on page
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    return render(request,'page_NotesList.html', {'page': page, 'notes': notes})

def view_NoteDetails(request, year, month, day, code):
    note = model_Note.objects.get(slug=code, publish__year=year, publish__month=month, publish__day=day)
    return render(request,'page_NoteDetails.html',{'note': note})

def view_InputNote(request):
    note = model_Note()
    saved = False
    if request.method == 'POST':
        form = InputNoteForm(request.POST)
        print("form1:", form)
        if form.is_valid():
            print("form2:", form)
            cd = form.cleaned_data
            note = form.save(commit=False)
            note.slug = cd['title'].replace(' ','').lower()
            note.author =  request.user
            note.save()
            saved = True
            return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})
        else:
            form = InputNoteForm()
            return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})
    else:
        form = InputNoteForm()
        return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})

