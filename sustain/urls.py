"""sustain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register.views import register,category
from login.views import log_in
from django.contrib.auth.views import LogoutView
from django.conf import settings
from blog.views import blog_view
from django.conf.urls.static import static
from ngo import urls
from leaderboard import urls
from quiz.views import quiz
from pledge.views import send_pledge
from orgs_and_ngos.views import orgs_view,ngos_view
from carbon_footprint.views import c_footprint
from articles.views import article
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls') ),
    path('blog/',include('blog.urls') ),
    path('register/', register, name='register' ),
    path('register/category', category, name='category' ), #added for category selection
    path('login/', log_in , name='login'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/',LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),name='logout'),
    path('',include('ngo.urls')),#for viewing and registring NGO,Indu,Indiv survey and ping
    path('',include('leaderboard.urls')),#for viewing and registring NGO,Indu,Indiv survey and ping
    path('quiz/',quiz, name='quiz' ),
    path('pledge/',send_pledge, name='pledge' ),##arithmeticpal
    
    path('orgs/', orgs_view, name='orgs' ),
    path('ngos/', ngos_view, name='ngos' ),
    path('carbon_footprint/', c_footprint, name='carbon_footprint' ),
    path('articles/',article, name='articles' ),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
