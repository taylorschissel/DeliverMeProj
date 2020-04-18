from django.urls import path
from . import views

urlpatterns = [
    path("http://DeliverMe.com", views.home, name="home"),
]

