from django.shortcuts import render
from datetime import datetime

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import  get_object_or_404, render
#from django.urls import reverse

#def home(request):
    #message = "This is the DeliverMe Website"
 #   current_user= "Taylor Schissel"
  #  return render(request, 'DeliverApp/home.html',{'date': datetime.now(), 'login': current_user})

def home(request):
    return render(request, 'homePage.html')