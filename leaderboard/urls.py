from django.urls import path, include
from . import views



urlpatterns = [

       path('register/result_main',views.result_main,name = "result_main"),
       path('leaderboard',views.lb,name = "leader_board"),
       path('carbon_daily',views.carbon_daily,name = "carbon_daily"),
       

]
