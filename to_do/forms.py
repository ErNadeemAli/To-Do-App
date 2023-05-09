from django import forms
from .models import Todo

class TodoFrom(forms.ModelForm):
    class Meta:
        model = Todo
        fields='__all__'
        widgets = {
          'details': forms.Textarea(attrs={'rows':8, 'cols':31}),
        }