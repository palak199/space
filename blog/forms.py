from django.forms import ModelForm
from .models import Blog

class post_form(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content' ,'images']

class BlogUpdateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content' ,'images']

