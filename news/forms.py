from django import forms
from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'date', 'full_text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'anons': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'full_text': forms.Textarea(attrs={'class': 'form-control'}),
        }