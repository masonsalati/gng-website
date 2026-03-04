from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
           'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'tel',
            'placeholder': 'e.g. 613-555-1234'
            }),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }