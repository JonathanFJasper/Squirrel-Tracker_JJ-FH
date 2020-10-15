from django.urls import path 

from . import views 


urlpatterns = [
        path('', views.index,name="index"),
        path('<Unique_Squirrel_ID>/details/',views.details,name="details"),
        ]
