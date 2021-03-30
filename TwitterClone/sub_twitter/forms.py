from django import forms
from .models import tweet

class PictureForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['name','image', 'body' ]
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Name'}),
            'body': forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Whats up Doc?'}),
          
        }



        