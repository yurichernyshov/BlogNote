from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import NoteSerializer
from .models import model_Note
from .forms import InputNoteForm


def view_StartPage(request):
    return render(request, 'page_StartPage.html')


def view_NotesList(request):
    objects_all = model_Note.objects.all()
    objects_list = []
    for obj in objects_all:
        if(obj.author == request.user) or (obj.status == "public"):
            objects_list.append(obj)

    paginator = Paginator(objects_list, 3)  # 3 articles on page
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
    return render(request, 'page_NoteDetails.html', {'note': note})


def view_InputNote(request):
    note = model_Note()
    saved = False
    if request.method == 'POST':
        form = InputNoteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            note = form.save(commit=False)
            note.slug = cd['title'].replace(' ', '').lower()
            note.author = request.user
            note.save()
            saved = True
            return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})
        else:
            form = InputNoteForm()
            return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})
    else:
        form = InputNoteForm()
        return render(request, 'page_InputNote.html', {'note': note, 'form': form, 'saved': saved})


class NoteAPIView(APIView):
    def get(self, request):
        notes = model_Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response({"notes": serializer.data})

    def post(self, request):
        note_saved = None
        note = request.data.get('note')
        serializer = NoteSerializer(data=note)
        if serializer.is_valid(raise_exception=True):
            note_saved = serializer.save()
        return Response({"success": "Note '{}' created successfully".format(note_saved.title)})


    def put(self, request, year, month, day, code):
        note_saved = None
        saved_note = get_object_or_404(model_Note.objects.all(), slug=code, publish__year=year, publish__month=month, publish__day=day)
        data = request.data.get('note')
        serializer = NoteSerializer(instance=saved_note, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            note_saved = serializer.save()
        return Response({"success": "Note '{}' updated successfully".format(note_saved.title)})

    def delete(self, request, pk):
        note = get_object_or_404(model_Note.objects.all(), pk=pk)
        note.delete()
        return Response({"message": "Note with id `{}` has been deleted.".format(pk)}, status=204)
