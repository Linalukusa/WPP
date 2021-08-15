from django import forms
from .models import Project
from django.core.exceptions import ValidationError

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['leadorganisations', 'projectname', 'publisher','city','projectlogo','maintheme','topic','website',
        'email','startdate','enddate','projectsummary','whatwedo','howwedo','achieved']


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['leadorganisations', 'projectname', 'publisher','city','projectlogo','maintheme','topic','website',
        'email','startdate','enddate','projectsummary','whatwedo','howwedo','achieved']