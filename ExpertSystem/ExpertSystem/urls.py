from django.conf.urls import include, url
import app.views
from app import forms, views
from django.urls import path



# Django processes URL patterns in the order they appear in the array
urlpatterns = [
   
    path('', views.problem, name='home'),
   
]
