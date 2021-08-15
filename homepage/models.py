from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class   Homepages (models.Model):
    content_1 = RichTextUploadingField(blank=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    background = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    maincontent = RichTextUploadingField (blank =True)
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.background
