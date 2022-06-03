from . import models
from django import forms

class URLForm(forms.ModelForm):
    class Meta():
        model = models.URLinput
        fields = ('URLvalue',)