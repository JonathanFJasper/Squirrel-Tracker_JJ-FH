from django.urls import math 

from . import views 


urlpatterns = [
        path('', views.index,name="index"),

        ]
