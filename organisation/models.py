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

class Organisation (models.Model):
    '''Model for managing discussions'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organisationname = models.CharField(max_length=500,blank=False, verbose_name='Organisation Name', )
    city = models.CharField(blank=True, max_length=500,verbose_name='City')
    province= models.IntegerField (choices=Provinces, verbose_name="Provinces", default=1, blank=False)
    projectlogo =models.ImageField(upload_to='documents/', blank=True, verbose_name='Research Paper')
    website = models.URLField(blank=True, verbose_name='Website')
    email = models.EmailField(blank=False, default="", verbose_name='Email')   
    mission = models.TextField(blank=False, verbose_name='Mission')
    vision = models.TextField(blank=False, verbose_name='Vision')
    achieved = models.TextField(blank=False, verbose_name='What We Have Achieved?')
    created_time = models.DateTimeField(auto_now_add=True, )
    def get_absolute_url(self):
        '''Returns the URL of the disc       ussion'''
        return "/organisation/%i/" % self.id

    class Meta:
        ordering = ['-created_time']

class OrganisationParticipant(models.Model):
    '''Model for managing a discussion's participant'''
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)