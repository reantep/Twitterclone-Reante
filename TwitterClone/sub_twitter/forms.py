from django import forms
from .models import tweet

class PictureForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['name', 'body', 'image', 'like_count', 'created_at', 'updated_at' ]
