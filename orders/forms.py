from django import forms
from .models import address


class addressform(forms.ModelForm):
    class Meta:
        model = address
        exclude = ['user']