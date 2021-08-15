from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


Provinces = (
    (1,'Select'),
    (2, ' Eastern Cape'),
    (3,'Free State'),
    (4,'Gauteng'),
    (5,'KwaZulu-Natal'),
    (6,'Limpopo'),
    (7,'Mpumalanga'),
    (8,'Northern Cape'),
    (9,'North West'),
    (10,'Western Cape'),
    (11,'All nationals'),
    (12,'International'),
)

class Project(models.Model):
    '''Model for managing discussions'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    leadorganisations = models.CharField(max_length=500, default="", verbose_name='Title', blank=False)
    projectname = models.CharField(max_length=500,blank=False, verbose_name='Lead Researcher', )
    publisher = models.CharField(max_length=500,blank=False,default="", verbose_name='Publisher')
    city = models.CharField(blank=True, max_length=500,verbose_name='City')
    projectlogo =models.FileField(upload_to='documents/', blank=True, verbose_name='Research Paper')
    maintheme = models.CharField(max_length=500,blank=False, verbose_name='Main Theme')
    topic = models.CharField(max_length=500,blank=False, verbose_name='Topic')
    website = models.URLField(blank=True, verbose_name='Website')
    email = models.EmailField(blank=False, default="", verbose_name='Email')   
    startdate = models.DateTimeField(null=True, blank=True, verbose_name='Start Date')
    enddate = models.DateTimeField(null=True, blank=True, verbose_name='End Date')
    projectsummary = RichTextField(blank=False, verbose_name='Research Summary')
    whatwedo = models.TextField(blank=False, verbose_name='Funding')
    howwedo = models.TextField(blank=False, verbose_name='How We Do?')
    achieved = models.TextField(blank=False, verbose_name='What We Have Achieved?')
    created_time = models.DateTimeField(auto_now_add=True, )

    def get_absolute_url(self):
        '''Returns the URL of the discussion'''
        return "/projects/%i/" % self.id

    class Meta:
        ordering = ['-created_time']

class ProjectParticipant(models.Model):
    '''Model for managing a discussion's participant'''
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)