from django import forms
from .models import toDoListItem

class toDoListItemForm(forms.ModelForm):
    class Meta:
        model = toDoListItem
        fields = ['text']