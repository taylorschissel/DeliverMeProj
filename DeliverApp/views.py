

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from DeliverApp.forms import DeliveryForm
from .models import DeliveryRequest
from django.views.generic import TemplateView


# Create your views here.

def newRequest(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.dateCreated = timezone.now()
            post.save()
            return redirect('requestDetail', pk=post.pk)
    else:
        form = DeliveryForm()
    return render(request, 'deliveryRequest.html', {'form': form})

def requestDetail(request, pk):
    post = get_object_or_404(DeliveryRequest, pk=pk)
    return render(request, 'requestDetails.html', {'post': post})

def requestList(request):
    posts = DeliveryRequest.objects.all()
    return render(request, 'requestList.html', {'posts': posts})

def home(request):
    return render(request, 'homePage.html', {})

#def isAccepted(request)
