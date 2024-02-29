from django import forms
from .models import template


class templateForm(forms.ModelForm):
    class Meta:
        model = template
        fields = [
            'project1Title', 'p1FinalImg', 'p1FinalCap', 'p1ProgressImg1', 'p1ProgressCap1', 'p1ProgressImg2', 'p1ProgressCap2', 'p1ProgressImg3', 'p1ProgressCap3', 'p1Explanation',
            'project2Title', 'p2FinalImg', 'p2FinalCap', 'p2ProgressImg1', 'p2ProgressCap1', 'p2ProgressImg2', 'p2ProgressCap2', 'p2ProgressImg3', 'p2ProgressCap3', 'p2Explanation',
            'project3Title', 'p3FinalImg', 'p3FinalCap', 'p3ProgressImg1', 'p3ProgressCap1', 'p3ProgressImg2', 'p3ProgressCap2', 'p3ProgressImg3', 'p3ProgressCap3', 'p3Explanation',
            'project4Title', 'p4FinalImg', 'p4FinalCap', 'p4ProgressImg1', 'p4ProgressCap1', 'p4ProgressImg2', 'p4ProgressCap2', 'p4ProgressImg3', 'p4ProgressCap3', 'p4Explanation',
        ]

