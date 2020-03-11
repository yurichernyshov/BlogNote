from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
   
from BlogNote.Notes.models import model_Note

class InputNoteForm(forms.ModelForm):
    class Meta:
        model = model_Note
        fields = ('title', 'body', 'status', 'latitude', 'longtitude', 'zoom')
        widgets = {'latitude'  : forms.HiddenInput(), 
                   'longtitude': forms.HiddenInput(), 
                   'zoom'      : forms.HiddenInput()}
