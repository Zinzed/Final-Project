from django import forms
from .models import template1


class template1Form(forms.ModelForm):
    class Meta:
        model = template1.project1
        fields = ['title',
                  ]
