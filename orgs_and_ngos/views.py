from django.shortcuts import render
from .models import orgs,ngos
# Create your views here.
from ngo.models import Ngo , Industry

def orgs_view(request):
    contents=Industry.objects.all()
    return render(request,'orgs.html',{'contents':contents})

def ngos_view(request):
    contents=Ngo.objects.all()
    return render(request,'ngos.html',{'contents':contents})