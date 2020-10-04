from django.shortcuts import render
import random
# Create your views here.
from django.shortcuts import render
import random
from bs4 import BeautifulSoup
import requests
from .models import Water_level
from json import dumps
from leaderboard.models import Carbon_fp
import datetime
from django.contrib.auth.models import User
from PIL import Image, ImageDraw, ImageFont
from django.core import serializers

# Create your views here.
def index(request):
    user = request.user
    carbon = Carbon_fp.objects.filter(user=user)
    carbon_data = []
    for i in carbon:
        new = {}
        new['y'] = i.carbon
        carbon_data.append(new)
        print(i.carbon)
    
    print(carbon_data)
    carbon = dumps({'c_data' : carbon_data})
    context = {
            
            'carbon':carbon,
    }
    print(carbon)
    return render(request, 'index.html',context)



    if not User.is_anonymous:
        # user = request.user.first_name
        # img = Image.open('main/static/images/certificate.jpg')
        # d1 = ImageDraw.Draw(img)
        # font = ImageFont.truetype("arial.ttf", 80)
        # d1.text((760, 450),user, fill=( 0,0,0,100),font = font)
        # img.save("main/static/images/image_text.jpg")
        
        try:
            score = 0
            
            source = requests.get('http://124.253.142.66').text
            soup=BeautifulSoup(source,'lxml')
            match=soup.p.text
           
           
            context = {
                
                'data':match,
                # 'dataJSON':dataJSON
            }
        
            user=request.user
            if user:
                today = datetime.datetime.now().date()
                x=Water_level.objects.filter(user=request.user).first()

                if x :
                    y=x.time.date()
                    if y==today:
                        return render(request,'index.html',context)
                    else:
                        new=Water_level.objects.create(user=request.user)
                        new.save()
                else:
                    new=Water_level.objects.create(user=request.user)
                    new.save()
                
                return render(request, 'index.html',context)
        except:
            carbon = Carbon_fp.objects.filter(user=user)
            carbon = serializers.serialize('json', carbon)
            carbon = dumps(carbon)
            # print(dataJSON)

            if request.user and request.user.category: 
                category = str(request.user.category)
                if (category == 'ngo') :
                    return render(request, 'index.html' , {'ngo': category,'carbon':carbon})
                elif (category == 'industry'):
                    return render(request, 'index.html' , {'industry': category,'carbon':carbon})
                elif (category == 'individual'):
                    return render(request, 'index.html' , {'industry': category,'carbon':carbon})
                else:
                    return render(request, 'index.html',{'carbon':carbon})
            else:
                return render(request, 'index.html',{'carbon':carbon})
    else : 
        # user =request.user
        # carbon = Carbon_fp.objects.filter(user=user)
        # carbon = serializers.serialize('json', carbon)
        
        # carbon = dumps(carbon)
        # print(dataJSON)

        # return render(request, 'index.html',{'carbon':carbon})
        return render(request, 'index.html')




        

def survey(request):
    return render(request,'survey-individual.html')   
def leaderboard(request):
    return render(request,'leaderboard.html')


