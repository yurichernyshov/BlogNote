from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from BlogNote.Notes.models import model_Note
from BlogNote.Notes.forms import InputNoteForm, TestForm

def view_StartPage(request):
    return render(request,'page_StartPage.html')

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
        if form.is_valid():
            cd = form.cleaned_data
            #save new note (title, body, status)
            note=form.save(commit=False)
            note.slug = cd['title'].replace(' ','').lower() # unique slug name
            note.author =  request.user

#    title = models.CharField(max_length=200)
#    slug = models.SlugField(max_length=250, unique_for_date='publish')
#    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='note_posts')
#    body = models.TextField()
#    publish = models.DateTimeField(default=timezone.now)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
#    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

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
    return render(request, 'test.html', {'form': form})

