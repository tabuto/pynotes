from django.contrib import admin
from mysite.pynotes.models import Note, NoteType

admin.site.register(Note)
admin.site.register(NoteType)
