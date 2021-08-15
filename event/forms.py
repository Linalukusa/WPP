from django import forms
from .models import Event
from django.core.exceptions import ValidationError


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','logo','website','email', 'description', 'location', 'start_time', 'end_time']