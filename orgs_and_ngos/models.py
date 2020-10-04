from django.db import models

# Create your models here.
class orgs(models.Model):
    Name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to= 'images/orgs', null=True)
    link = models.URLField(max_length=200,null=True)

class ngos(models.Model):
    Name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to= 'images/ngos', null=True)
    link = models.URLField(max_length=200,null=True)
