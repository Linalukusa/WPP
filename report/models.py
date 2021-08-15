from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

Severity = (
    (1,'Select'),
    (2, 'Critical'),
    (3,'Major'),
    (4,'Moderate'),
    (5,'Minor'),
    (6,'Cosmetic'),
)
Priority=(
    (1,'Low'),
    (2, 'Medium'),
    (3,'High'),
)
Reproducibility=(
    (1,'10%'),
    (2,'25%'),
    (3,'50%'),
    (4,'75%'),
    (5,'100%'),
)
class Report(models.Model):
    '''Model for managing discussions'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resourcetitle = models.CharField(blank=False,max_length=500, )
    severity = models.IntegerField(choices=Severity,blank="false", default=1, verbose_name='Severity')
    Priority = models.IntegerField(choices=Priority,blank="false", default=1, verbose_name='Priority')
    Reproducibility = models.IntegerField(choices=Reproducibility,blank="false", default=1, verbose_name='Reproducibility')
    media =models.ImageField(upload_to='images/', blank=True, verbose_name='Provide Picture/Video')
    Description= RichTextField(blank=False,default="", verbose_name='Description of the Issue')
    created_time = models.DateTimeField(auto_now_add=True,)
    def get_absolute_url(self):
        '''Returns the URL of the discussion'''
        return "/report/%i/" % self.id

    class Meta:
        ordering = ['-created_time']

class ReportParticipant(models.Model):
    '''Model for managing a discussion's participant'''
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)