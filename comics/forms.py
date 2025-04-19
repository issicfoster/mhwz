from django import forms
from .models import Comic

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'author', 'description', 'file']
    