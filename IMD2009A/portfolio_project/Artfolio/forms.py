from django import forms
from .models import template1


class template1Form(forms.ModelForm):
    class Meta:
        model = template1
        fields = ['project1Title',
                  'project1FinalImg',
                  'project1FinalImgCap',
                  'project1Explanation',
                  ]
