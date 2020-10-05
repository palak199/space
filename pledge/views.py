from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.contrib import messages
from django.template.loader import render_to_string
import smtplib 
from sustain.settings import EMAIL_HOST_USER
from django.core.mail import send_mail



# Create your views here.
def send_pledge(request):  

    if request.method == 'POST':
        subject = "Pledge signed"
        plain_message="Congrats."
        message = render_to_string('pledge-signed.html')
        message.content_subtype = "html"
        receiver = request.user.email  
        receivers = [receiver]
        user=request.user
       
        receivers.append(user)
        
        print(receivers)
        send_mail(subject, plain_message, EMAIL_HOST_USER, receivers,html_message=message)
        return redirect('home')
            
    return render(request,"pledge.html")

   
       
    



   
            


  
  

