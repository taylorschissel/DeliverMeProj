

from django.db import models

# Create your models here.
from django.utils import timezone


class DeliveryRequest(models.Model):

    pickupName = models.CharField(max_length=30)
    pickupStreetAddress = models.CharField(max_length=100)
    pickupCity = models.CharField(max_length=20)
    pickupState = models.CharField(max_length=2)
    pickupZipcode = models.CharField(max_length=5)

    dropoffName = models.CharField(max_length=30)
    dropoffStreetAddress = models.CharField(max_length=100)
    dropoffCity = models.CharField(max_length=20)
    dropoffState = models.CharField(max_length=2)
    dropoffZipcode = models.CharField(max_length=5)

    item = models.CharField(max_length=30)
    description = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    #categories = models.ManyToManyField('Category', related_name='posts')
    lastModified = models.DateTimeField(auto_now=True)

    def publish(self):
        self.dateCreated = timezone.now()
        self.save()

class Category(models.Model):

    name = models.CharField(max_length=20)

class Topic(models.Model):
    name = models.CharField(max_length=20)