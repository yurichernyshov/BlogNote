from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class model_Note(models.Model):
    STATUS_CHOICES = (
        ('private', 'Private'),
        ('public',  'Public'),
    )
    title      = models.CharField(max_length=200)
    slug       = models.SlugField(max_length=250, unique_for_date='publish')
    author     = models.ForeignKey(User, on_delete=models.CASCADE,related_name='note_posts')
    body       = models.TextField()
    publish    = models.DateTimeField(default=timezone.now)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)
    status     = models.CharField(max_length=10, choices=STATUS_CHOICES, default='private')
    latitude   = models.FloatField()
    longtitude = models.FloatField()
    zoom       = models.IntegerField()

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return (self.title)

    def get_absolute_url(self):
        return reverse('Notes:note_details', args=[self.publish.year,self.publish.month, self.publish.day, self.slug])

