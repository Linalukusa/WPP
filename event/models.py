from django.db import models
from django.conf import settings


class Event(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, verbose_name='Event Name')
    description = models.TextField(blank=False, verbose_name='Description')
    created_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='Start Date')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='End Date')
    location = models.CharField(max_length=150, verbose_name='Location')
    logo =models.ImageField(upload_to='documents/', blank=True, verbose_name='Event Logo')
    website = models.URLField(blank=True, verbose_name='Website')
    email = models.EmailField(blank=False, verbose_name='Email', default="")

    def get_absolute_url(self):
        """
        This method return the relative url for viewing a single event
        :return: the relative url as string
        """
        return "/events/%i/" % self.id

    class Meta:
        ordering = ['-created_time']


#class EventParticipant(models.Model):
    """
    This model is for saving event's participants. Everytime an user is invited, a new object is created and
    by default they didn't accept it yet.
    """
    #inviter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inviter')
    #invitee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invitee')
    #event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #created_time = models.DateTimeField(auto_now_add=True)
    #accepted = models.BooleanField(default=False)