from django.shortcuts import render
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets

# Create your views here.

class ListingViewsets(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
class BookingViewsets(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer  
