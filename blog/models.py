from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils import timezone


Trend_CHOICES = (
   ('Y', 'Yes'),
   ('N', 'No')
)

user=User
class Blog (models.Model):
    
    title        = models.CharField(max_length=50)
    content      = HTMLField()
    author       = models.ForeignKey(User, on_delete=models.CASCADE) 
    images       = models.ImageField(upload_to= 'images/blog', null=True)
    likes       =  models.ManyToManyField(User,blank=True, related_name='likes')
    time        =  models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time',]

    @property
    def total_likes(self):
        return self.likes.count() 

    def __str__(self):
        return self.title 
