from django.shortcuts import render
import random

# Create your views here.
def quiz(request):
    return render(request,'quiz.html',{'quiz':quiz}) 