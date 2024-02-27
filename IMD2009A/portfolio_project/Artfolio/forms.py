from django import forms
from .models import template


class templateForm(forms.ModelForm):
    class Meta:
        model = template
        fields = ['project1Title', 'p1FinalCap', 'p1ProgressCap1', 'p1ProgressCap2', 'p1ProgressCap3',
                  'project2Title', 'p2FinalCap', 'p2ProgressCap1', 'p2ProgressCap2', 'p2ProgressCap3',
                  'project3Title', 'p3FinalCap', 'p3ProgressCap1', 'p3ProgressCap2', 'p3ProgressCap3',
                  'project4Title', 'p4FinalCap', 'p4ProgressCap1', 'p4ProgressCap2', 'p4ProgressCap3',
                  ]
