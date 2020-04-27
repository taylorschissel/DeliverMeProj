from django import forms
from .models import DeliveryRequest

#this class creates the form used when creating a new delivery request
class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ('item',
                  'description',
                  'pickupName',
                  'pickupStreetAddress',
                  'pickupCity',
                  'pickupState',
                  'pickupZipcode',
                  'dropoffName',
                  'dropoffStreetAddress',
                  'dropoffCity',
                  'dropoffState',
                  'dropoffZipcode',)
        labels = {
            'item':'Item',
          'description':'Description',
          'pickupName':'Pickup Name',
          'pickupStreetAddress':'Street Address',
          'pickupCity':'City',
          'pickupState':'State',
          'pickupZipcode':'Zipcode',
          'dropoffName':'Dropoff Name',
          'dropoffStreetAddress':'Street Address',
          'dropoffCity':'City',
          'dropoffState':'State',
          'dropoffZipcode':'Zipcode',
        }
