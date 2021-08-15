from django import forms
from .models import *
from django.core.exceptions import ValidationError


class DiscussionCreationForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'description']


class DiscussionUpdateForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'description']


class DiscussionCommentForm(forms.ModelForm):
    '''A form that is used to create a new comment to a discussion'''
    content = forms.CharField(required=True)

    class Meta:
        model = DiscussionComment
        fields = [ 'content' ]