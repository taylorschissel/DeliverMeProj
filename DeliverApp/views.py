from datetime import timezone

from django.shortcuts import render, redirect, get_object_or_404
from DeliverApp.forms import DeliveryForm
from django.views.generic import TemplateView


# Create your views here.

def newRequest(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.dateCreated = timezone.now()
            post.save()
            return redirect('requestDetail', pk=post.pk)
    else:
        form = DeliveryForm()
    return render(request, 'deliveryRequest.html', {'form': form})
'''
def requestDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
'''
def home(request):
    return render(request, 'homePage.html')
'''
class DeliveryView(TemplateView):
    template_name= 'deliveryRequest.html'

    def get(self, request):
        form = DeliveryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DeliveryForm(request.POST)
        if form.is_valid():
            #form.save()
            text = form.cleaned_data['pickupName','pickupStreetAddress', 'pickupCity', 'pickupState', 'pickupZipCode', 'dropoffName', 'dropoffStreetAddress', 'dropoffCity', 'dropoffSate','dropoffZipCode','item','description']
            form = DeliveryForm()
            return redirect('deliveryRequest')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

'''