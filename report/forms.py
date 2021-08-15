from django import forms
from .models import Report
from django.core.exceptions import ValidationError

class ReportCreationForm(forms.Form):
    '''A form that is used to create a new discussion'''
    title = forms.CharField(required=True,max_length=500, )
    description = forms.CharField(required=True, max_length=500,)
    publisher = forms.CharField(required=False, max_length=500,)
    publicationdate = forms.DateTimeField(input_formats=['%Y/%m/%d'], required=False)
    files = forms.CharField(widget=forms.Textarea, required=True, )
    websitelink = forms.CharField(widget=forms.Textarea, required=True, )
    videolink = forms.CharField(widget=forms.Textarea, required=True, )
    created_time = forms.DateTimeField()

    def clean(self):
        '''Makes sure the form is valid'''
        super(forms.Form, self).clean()

        if self.cleaned_data.get('leadorganisations') == '':
            raise ValidationError("Lead Organisation is mandatory")
    def __init__(self,*args, **kwargs):
            super( ReportCreationForm, self).__init__(*args, **kwargs)
            self.fields['startdate'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'date-selector'}))
            self.fields['enddate'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'date-selector'})) 


    def clean_start_date(self):
            return datetime.datetime.strptime(self.cleaned_data['startdate'], '%Y-%m-%d')
    def clean_end_date(self):
            return datetime.datetime.strptime(self.cleaned_data['enddate'], '%Y-%m-%d')

    class Meta:
        model = Report
        fields = ['title', 'description', 'publisher','publicationdate','files','websitelink','videolink',]

class ReportUpdateForm(forms.ModelForm):
    '''A form that is used to update an existing discussion's details'''
    title = forms.CharField(required=True,max_length=500, )
    description = forms.CharField(required=True, max_length=500,)
    publisher = forms.CharField(required=False, max_length=500,)
    publicationdate = forms.DateTimeField(input_formats=['%Y/%m/%d'], required=False)
    files = forms.CharField(widget=forms.Textarea, required=True, )
    websitelink = forms.CharField(widget=forms.Textarea, required=True, )
    videolink = forms.CharField(widget=forms.Textarea, required=True, )
    created_time = forms.DateTimeField()

    class Meta:
        model = Report
        fields = ['title', 'description', 'publisher','publicationdate','files','websitelink','videolink',]