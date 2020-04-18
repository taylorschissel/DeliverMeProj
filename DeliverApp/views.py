from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    message = "This is the DeliverMe Website"
    return HttpResponse(message)
