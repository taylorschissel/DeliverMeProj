from django import forms
from .models import DeliveryRequest

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ('pickupName', 'dropoffName',)


   #user presses submit request: redirected to success page, updates when a driver has accepted the request
   #user presses submit request: request is redirectd to accept page