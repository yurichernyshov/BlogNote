"""BlogNote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from BlogNote.MainPage.views import view_NotesList, view_NoteDetails, view_InputNote, view_Test

app_name = "BlogNote"

urlpatterns = [
     url(r'([0-9]{4})/([0-9]+)/([0-9]+)/([0-9]{4})', view_NoteDetails, name='note_details'),
     url('InputNote', view_InputNote, name='input_note'),
     url('Test', view_Test, name='test'),
     url('', view_NotesList, name='notes_list'),
]
