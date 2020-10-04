from django.db import models
# from tinymce.models import HTMLField

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=100)
    content      = models.TextField()
    images       = models.ImageField(upload_to= 'images/article', null=True)


    def __str__(self):
        return self.title

    