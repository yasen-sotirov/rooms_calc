# myapp/forms.py

from django import forms
from .models import TextEntry

class TextEntryForm(forms.ModelForm):
    class Meta:
        model = TextEntry
        fields = ['content']
