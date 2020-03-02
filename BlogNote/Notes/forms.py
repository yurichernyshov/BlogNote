from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from BlogNote.Notes.models import model_Note

class InputNoteForm(forms.ModelForm):
    class Meta:
        model = model_Note
        fields = ('title', 'body', 'status')

class TestForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
