from django.db import models
from django.conf import settings


class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()

  def __str__(self):
    return self.title

    
class Research(models.Model):
    '''Model for managing discussions'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default="", verbose_name='Title')
    leadresearcher = models.CharField(max_length=500,blank=False, verbose_name='Lead Researcher')
    researchfile =models.FileField(upload_to='documents/', blank=True, verbose_name='Research Paper')
    publisher = models.CharField(max_length=500,blank=False,  verbose_name='Publisher')
    city = models.CharField(blank=True, max_length=500, verbose_name='City')
    startdate = models.DateTimeField(null=True, blank=True, verbose_name='Start Date')
    enddate = models.DateTimeField(null=True, blank=True, verbose_name='End Date')
    description= models.TextField(blank=False,default="", verbose_name='Research Summary')
    collab = models.TextField(blank=True, verbose_name='Collaboration')
    funding = models.TextField(blank=True, verbose_name='Funding')
    website = models.URLField(blank=True, verbose_name='Website')
    email = models.EmailField(blank=False, verbose_name='Email')
    created_time = models.DateTimeField(auto_now_add=True, )

    def get_absolute_url(self):
        '''Returns the URL of the discussion'''
        return "/researchs/%i/" % self.id


    class Meta:
        ordering = ['-created_time']

class ResearchParticipant(models.Model):
    '''Model for managing a discussion's participant'''
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)