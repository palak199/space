from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def log_in(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            
            return redirect('home')
            
        else:
            messages.info(request, 'Invalid Credentials')

            return redirect('login')

    return render(request,'login.html' )

