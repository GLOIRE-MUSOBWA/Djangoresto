from django import forms
from django.forms import fields
from restorantbar.models import table

class Restorantbarform(forms.ModelForm):
    class Meta:
        model=table
        fields="__all__"