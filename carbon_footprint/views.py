from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Carbon_footprint
import datetime




# Create your views here.
def c_footprint(request):
    today = datetime.datetime.now().date()
    x=Carbon_footprint.objects.filter(user=request.user)
    if x :
        x=x[0].date
        if x==today:
            return render(request,'404.html')
    if request.method=='POST':
        x=Carbon_footprint.objects.create(
            user=request.user,
            electric= request.POST["electric"], 
            gas=request.POST["gas"],
            oil=request.POST["oil"],
            car=request.POST["car"],
            flights=request.POST["flights"],
            day  =request.POST["dayOptionsRadios"],
            meal=request.POST["mealOptionsRadios"],
        )
        x.save()

        return redirect('carbon_daily')
    return render(request , 'carbon_footprint.html')