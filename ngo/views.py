from django.shortcuts import render, redirect
from .models import Ngo, Individual, Industry
from register.models import Category
# Create your views here.
from .forms import NGO_form


def ngo_survey(request):

    if request.method == "POST":
        form  = NGO_form (request.POST, request.FILES)
        form.instance.user=request.user
        if 1:
            print(form)
            form.save()
            return  redirect('home')
    
    else:
        form = NGO_form()
        

    return render(request, 'ngo-survey.html' , {'form' : form})


def indv_survey(request):

    if request.method == "POST":
        x = Individual.objects.create(
            user=request.user,
            tank_cap=request.POST["tank_cap"],
            member=request.POST["member"],
            garbage=request.POST["garbage"],
            waste_water=request.POST["waste_water"],
            biodegradable=request.POST["biodegradable"],
            recycle=request.POST["recycle"],
            govt=request.POST["govt"],
            disposal=request.POST["disposal"],
            energy=request.POST["energy"],
            bulb=request.POST["bulb"],
            cfc=request.POST["cfc"],
            news=request.POST["news"],
            plant=request.POST["plant"],
            travel=request.POST["travel"],
            diet=request.POST["diet"],
        )
        x.save()
        return redirect('result_main')

    return render(request, "individual-survey.html")


def indus_survey(request):
    if request.method == "POST":
        x = Industry.objects.create(
            user=request.user,
            name=request.POST["name"],
            turnover=request.POST["turnover"],
            pollution=request.POST["pollution"],
            sustainibility=request.POST["sustainibility"],
            csr_def=request.POST["csr_def"],
            plant=request.POST["plant"],
            untreated_sewage=request.POST["untreated_sewage"],
            emp_month=request.POST["emp_month"],
            env_audit=request.POST["env_audit"],
            garbage=request.POST["garbage"],
            employment=request.POST["employment"],
            health=request.POST["health"],
            recycle=request.POST["recycle"],
            responsibility=request.POST["responsibility"],
            energy=request.POST["energy"],
            water_source=request.POST["water_source"],
            effluent=request.POST["effluent"],
            effluent_q=request.POST["effluent_q"],
            nature_waste=request.POST["nature_waste"],
        )
        x.save()
        return redirect('result_main')
    return render(request, 'industry-survey.html')
