from django import forms
from django.forms import ModelForm
from .models import *


class Search(forms.ModelForm):
    class Meta:
        model = SearchHistory
        fields = '__all__'
