from django import forms
from .models import Page


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','content','order']
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el título'}),
            'content': forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese el contenido'}),
            'order': forms.NumberInput(attrs={'class':'form-control'})
        }
        labels = {
            'title': '',
            'order': '',
            'content': ''
        }