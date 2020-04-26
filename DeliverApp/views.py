from django.shortcuts import render, redirect
from DeliverApp.forms import DeliveryForm
from django.views.generic import TemplateView


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

class DeliveryView(TemplateView):
    template_name= 'deliveryRequest.html'

    def get(self, request):
        form = DeliveryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['pickupName','pickupStreetAddress', 'pickupCity', 'pickupState', 'pickupZipCode', 'dropoffName', 'dropoffStreetAddress', 'dropoffCity', 'dropoffSate','dropoffZipCode','item','description']
            return redirect('DeliverApp:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)