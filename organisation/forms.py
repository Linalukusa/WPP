from django import forms
from .models import Organisation, OrganisationParticipant
from django.core.exceptions import ValidationError

class OrganisationCreationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['organisationname','city','province','projectlogo','vision','mission','website',
        'email', 'achieved']


class OrganisationUpdateForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['organisationname','city','province','projectlogo','vision','mission','website',
        'email', 'achieved']