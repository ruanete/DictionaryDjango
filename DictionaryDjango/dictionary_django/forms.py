from django import forms
from .models import term, definition


class termForm(forms.ModelForm):
    class Meta:
        model = term
        fields = ['word']


class definitionForm(forms.ModelForm):
    class Meta:
        model = definition
        fields = ['meaning', 'word_meaning_relationship']


