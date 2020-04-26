from django import forms
from DeliverApp.models import deliveryRequest

class DeliveryForm(forms.ModelForm):
    fName = forms.CharField(label='First Name:', max_length=15)
    lName = forms.CharField(label='Last Name', max_length=20)
    address = forms.CharField(label='Street Address', max_length=50)
    city = forms.CharField(label='City:', max_length=20)
    state = forms.CharField(label='State:', max_length=20)

    class Meta:
        model = deliveryRequest
        fields = ['pickupName', 'pickupStreetAddress', 'pickupCity', 'pickupState', 'pickupZipcode', 'dropoffName', 'dropoffStreetAddress', 'dropoffCity', 'dropoffState', 'dropoffZipcode', 'item', 'description']



   #user presses submit request: redirected to success page, updates when a driver has accepted the request
   #user presses submit request: request is redirectd to accept page