from django.db import models
from django.contrib.auth.models import User

choice_type = (
        ('ngo', 'ngo'),
        ('industry', 'industry'),
        ('individual', 'individual'),
    )
    # choices for type of Organization


class Category(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=25, choices=choice_type) ##for selecting the category of regestring person   

    def __str__(self):

        return self.category
