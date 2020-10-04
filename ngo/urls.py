from django.urls import path, include
from . import views


urlpatterns = [

    path('register/ngo-survey',views.ngo_survey,name = "ngo_survey"),
    path('register/indv-survey',views.indv_survey,name = "indv_survey"),
    path('register/indus-survey',views.indus_survey,name = "indus_survey"),
]
