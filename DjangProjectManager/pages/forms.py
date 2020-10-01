from django import forms
from .models import toDoListItem

class toDoListItemForm(forms.ModelForm):
    class Meta:
        model = toDoListItem
        fields = ['text']

class projectForm(forms.Form):
    accessChoices = [
        ('public', 'public'),
        ('private', 'private'),
    ]
    fieldChoices = [
        ('Requirements', 'Requirements'),
        ('Wireframes', 'Wireframes'),
        ('logo', 'logo'),
        # ('Designing', 'Designing'),
        ('Development', 'Development')
    ]
    # name = forms.CharField(max_length=100)
    # description = forms.CharField(max_length= 1000)
    # access = forms.CharField(widget=forms.RadioSelect(choices=accessChoices))
    fields = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=fieldChoices,
    )