from django import forms
from .models import template


class templateForm(forms.ModelForm):
    class Meta:
        model = template.project1
        fields = ['title',
                  ]
