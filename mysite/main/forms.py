from django import forms
from .models import ToDoList

class CreateNew(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)

    