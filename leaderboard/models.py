from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Indus_lb(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    score               = models.IntegerField()
    class Meta:
        ordering = ['-score']


class Indv_lb(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    score               = models.IntegerField()
    class Meta:
        ordering = ['-score']


class Carbon_fp(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    carbon  = models.IntegerField()
    date  = models.DateField(default=timezone.now)

    class Meta:
        ordering=['carbon']


