from django.shortcuts import render ,redirect
from ngo.models import Industry,Individual
from register.models import Category
from django.contrib.auth.models import User
from .models import Indus_lb,Indv_lb,Carbon_fp
from carbon_footprint.models import Carbon_footprint
from django.utils import timezone
import datetime


# Create your views here.



def result_main(request):
    user = request.user
    cat = Category.objects.filter(user=request.user)
    category =  cat[0].category

    # if category == 'ngo':
    if category == 'industry':
        score = 0
        data = Industry.objects.filter(user=user)
        for i in data:
            if i.pollution == 'yes':
                score = score + 10
            if i.sustainibility =='yes':
                score = score +5
            if i.plant =='yes':
                score = score +10
            if i.untreated_sewage =='no':
                score = score + 10
            if i.untreated_sewage =='yes':
                score = score -15
            if i.emp_month =='yes':
                score = score +15
            if i.env_audit =='yes':
                score = score + 15
            if i.garbage =='to some extent':
                score = score + 5
            if i.garbage =='a lot':
                score = score + 15
            if i.employment =='a lot':
                    score = score + 10
            if i.employment =='to some extent':
                score = score + 5
            if i.health =='a lot':
                score = score + 10
            if i.health =='to some extent':
                score = score + 5
            if i.recycle =='a lot':
                score = score + 15
            if i.recycle =='to some extent':
                score = score + 5
            if i.responsibility =='a lot':
                score = score + 15
            if i.responsibility =='to some extent':
                score = score + 5
            if i.energy == 'non_conventional':
                score = score + 15
            if i.energy == 'mix':
                score = score + 5
            if i.water_source == 'River/lake':
                score = score + 10
            if i.water_source == 'Ground water' or i.water_source == 'Municipal water':
                score = score + 5
            if i.water_source == 'Rain water':
                score = score + 20
            if i.effluent_q == '>50%':
                score = score - 20
            if i.effluent_q == '30%':
                score = score - 15
            if i.effluent_q == '20%':
                score = score - 10
            if i.effluent_q == '1%':
                score = score + 5
            final = (score/180)*100
            try:
                x = Indus_lb.objects.create(
                    user=request.user,
                    score = final,
                )
                x.save()
                score_in = Indus_lb.objects.filter(user=user)
                return render(request,'result-main.html',{'score_in':score_in})
            except:
                score_in = Indus_lb.objects.filter(user=user)
                return render(request,'result-main.html',{'score_in':score_in})
                
    if category == 'individual':
        score = 0
        data = Individual.objects.filter(user=user)
        for i in data:
        

            if i.garbage =='to some extent':
                score = score + 5
            if i.garbage =='a lot':
                score = score + 15
                
            if i.waste_water == 'a lot':
                score = score -10
            if i.waste_water == 'to some extent':
                score = score -5
            if i.waste_water == 'not at all':
                score = score +10

            if i.biodegradable == 'a lot':
                score = score +15
            if i.biodegradable == 'to some extent':
                score = score +10
            if i.biodegradable == 'not at all':
                score = score +0


            if i.recycle == 'a lot':
                score = score +15
            if i.recycle == 'to some extent':
                score = score +10
            if i.recycle == 'not at all':
                score = score +0


            if i.govt == 'a lot':
                score = score +15
            if i.govt == 'to some extent':
                score = score +10
            if i.govt == 'not at all':
                score = score +0

            if i.disposal == 'a lot':
                score = score -10
            if i.disposal == 'to some extent':
                score = score -5
            if i.disposal == 'not at all':
                score = score +10

            if i.energy == 'a lot':
                score = score +15
            if i.energy == 'to some extent':
                score = score +10
            if i.energy == 'not at all':
                score = score -5

            if i.bulb == 'yes':
                score = score +10
            if i.bulb == 'no':
                score = score -5

            if i.cfc == 'yes':
                score = score -10
            if i.cfc == 'no':
                score = score +10
            
            if i.news == 'yes':
                score = score +10
            if i.news == 'no':
                score = score +0

            if i.plant == 'yes':
                score = score +25
            if i.plant == 'no':
                score = score +0

            if i.travel == 'public':
                score = score +15
            if i.travel == 'private':
                score = score +0
            if i.travel == 'carpool':
                score = score +10
            
            if i.plant == 'veg':
                score = score +25
            if i.plant == 'non_veg':
                score = score +0
            if i.plant == 'mostly veg':
                score = score +5
               
            final = (score/180)*100
            try:
                x = Indv_lb.objects.create(
                    user=request.user,
                    score = final,
                )
                x.save()
                score_in = Indv_lb.objects.filter(user=user)
                return render(request,'result-main.html',{'score_in':score_in})
            except:
                score_in = Indv_lb.objects.filter(user=user)
                return render(request,'result-main.html',{'score_in':score_in})
        
    return render(request,'result-main.html')

def carbon_daily(request):
    today = datetime.datetime.now().date()
    user = request.user
    x=Carbon_fp.objects.filter(user=request.user)
    if x :
        x=x[0].date
        if x==today:
            score_in = Carbon_fp.objects.filter(date = today).filter(user=user)
            return render(request,'result-main.html',{'score_in':score_in})
    data = Carbon_footprint.objects.filter(date=today).filter(user=user)
    carb_fp=0
    print(data[0].electric)
    for i in data:
        carb_fp = carb_fp + float(i.electric)*0.75
        carb_fp = carb_fp + (float(i.gas)*0.3*1665)/1000
        carb_fp = carb_fp + (float(i.oil)*2500)/1000
        carb_fp = carb_fp + (float(i.car)*123)/1000
        carb_fp = carb_fp + (float(i.flights)*90)
        if i.meal =='yes':
            carb_fp = carb_fp + 0.4
        else:
            carb_fp = carb_fp +0.7
            
        x = Carbon_fp.objects.create(
            user= user,
            carbon = carb_fp
        )
        x.save()

    score_in = Carbon_fp.objects.filter(date = today).filter(user=user)
    return render(request,'result-main.html',{'score_in':score_in})

    # return render(request ,'result-main.html')



def lb(request):


    indus  = Indus_lb.objects.all()
    indv   = Indv_lb.objects.all()

    today = datetime.datetime.now().date()
    x=Carbon_fp.objects.filter(date=today)




    context = {
        'indus':indus,
        "indv" :indv,
        'carbon_fp':x,
    }



    return render(request,'leaderboard.html',context)
