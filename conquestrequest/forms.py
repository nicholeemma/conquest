from django import forms
from .models import Item


class ItemForm(forms.Form):
    name = forms.CharField(max_length=30,required= True)
    description = forms.CharField(max_length=100,required=True)
    filelink = forms.CharField(max_length=500,required=True)