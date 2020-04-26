from django import forms
from .models import DeliveryRequest

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ('item','description','pickupName','pickupStreetAddress','pickupCity','pickupState','pickupZipcode','dropoffName','dropoffStreetAddress','dropoffCity','dropoffState','dropoffZipcode',)

