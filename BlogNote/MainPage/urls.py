"""BlogNote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from BlogNote.MainPage.views import view_NotesList, view_NoteDetails, view_InputNote, view_Test

app_name = "BlogNote"

urlpatterns = [
     path(r'<int:year>/<int:month>/<int:day>/<slug:code>', view_NoteDetails, name='note_details'),
     path('InputNote', view_InputNote, name='input_note'),
     path('Test', view_Test, name='test'),
     path('', view_NotesList, name='notes_list'),
]



