from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class InputNoteForm(forms.Form):
    users  = User.objects.all()
    title  = forms.CharField(max_length=200)
    body   = forms.CharField(widget=forms.Textarea)
#    author = forms.ChoiceField(choices=((user, user) for user in users))
#    status = forms.ChoiceField(choices=((1, "draft"), (2, "published")))

class TestForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
