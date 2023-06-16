from django import forms
from django.forms import fields
from restorantbar.models import table
from restorantbar.models import reservation

class Restorantbarform(forms.ModelForm):
    class Meta:
        model=table
        fields="__all__"
        

class Restorantbarforms(forms.ModelForm):
    class Meta:
        model=reservation
        fields="__all__"        