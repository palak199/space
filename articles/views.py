from django.shortcuts import render
from .models import Article

# Create your views here.
def article(request):

    article  = Article.objects.all()

    return render(request , 'article.html',{'article':article})