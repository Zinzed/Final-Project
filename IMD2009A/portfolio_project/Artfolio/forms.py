from .models import template, filterTag
# from IMD2009A.portfolio_project.Artfolio.models import filterTag
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms


# Registration
class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Authentication

class loginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class templateForm(forms.ModelForm):
    class Meta:
        model = template

        fields = [
            'filterTags',

            'project1Title', 'p1FinalImg', 'p1FinalCap', 'p1ProgressImg1', 'p1ProgressCap1', 'p1ProgressImg2',
            'p1ProgressCap2', 'p1ProgressImg3', 'p1ProgressCap3', 'p1Explanation',

            'project2Title', 'p2FinalImg', 'p2FinalCap', 'p2ProgressImg1', 'p2ProgressCap1', 'p2ProgressImg2',
            'p2ProgressCap2', 'p2ProgressImg3', 'p2ProgressCap3', 'p2Explanation',

            'project3Title', 'p3FinalImg', 'p3FinalCap', 'p3ProgressImg1', 'p3ProgressCap1', 'p3ProgressImg2',
            'p3ProgressCap2', 'p3ProgressImg3', 'p3ProgressCap3', 'p3Explanation',

            'project4Title', 'p4FinalImg', 'p4FinalCap', 'p4ProgressImg1', 'p4ProgressCap1', 'p4ProgressImg2',
            'p4ProgressCap2', 'p4ProgressImg3', 'p4ProgressCap3', 'p4Explanation',

        ]

    filterTags = forms.ModelMultipleChoiceField(
        queryset=filterTag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
