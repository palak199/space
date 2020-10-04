from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bs4 import BeautifulSoup
import requests

# Create your models here.
class Water_level(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE) 
    water_level = models.IntegerField()
    time        =  models.DateTimeField(default=timezone.now)


    class Meta : 
        ordering=['-time']
        
    def save(self, *args, **kwargs): 
        source = requests.get('http://124.253.142.66').text
        soup=BeautifulSoup(source,'lxml')
        match=soup.p.text
        self.water_level =  match
        super(Water_level, self).save(*args, **kwargs) 