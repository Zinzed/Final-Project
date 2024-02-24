from django import forms
from .models import template


class templateForm(forms.ModelForm):
    class Meta:
        model = template
        fields = ['project1Title', 'project2Title',
                  ]
