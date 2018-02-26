from django import forms
from . import models


class NewWordForm(forms.ModelForm):
    class Meta:
        model = models.Word
        fields = ('word', 'sentence',)
