from django import forms
from .models import tweet

class PictureForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['name','image', 'body' ]
