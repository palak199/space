from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Category

def category(request):  ##For category registration
    if request.method=='POST':
        print('request.POST["category"],') 
        category  = request.POST["category"] 
            
        x=Category.objects.create(
            user=request.user,
            category  = request.POST["category"], 
        )
        x.save()
        # User = request.user
        cat = Category.objects.filter(user=request.user)
        category =  cat[0].category
        if category == 'ngo':
            return redirect('ngo_survey')
        if category == 'industry':
            return redirect('indus_survey')
        if category == 'individual':
            return redirect('indv_survey')
    else:
        return render (request, 'category.html')
    
def register(request):
    if request.method == 'POST':
        first_name  = request.POST["first_name"]
        last_name   = request.POST["last_name"]
        password1   = request.POST["password1"]
        password2   = request.POST["password2"]
        email       = request.POST["email"]
        if password1 == password2:

            if User.objects.filter(email=email).exists():

                messages.info(request, 'Email is already taken')

            else :

                user        = User.objects.create_user(username = email,password = password1,email = email,first_name=first_name,last_name=last_name)
                user.save()
                login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                messages.info(request, "Signup Successful. You need to fill the following information")
                return redirect('category')
        else:
            print('passwords dont match')
            messages.info(request, "Passwords dont match")
            return redirect('register')
    return render (request, 'register.html')