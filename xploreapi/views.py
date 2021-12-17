from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DestinationSerializer, \
    TourCompaniesSerializer, CarHireSerializer, HotelsSerializer, TourguidesSerializer, TweetsSerializer, \
    FactsSerializer, TripsSerializer, updatesSerializer, AnimalsSerializer, ActivitiesSerializer

from .models import Destinations, Trips, Tourguides, TourCompanies, Animals, Tweets, updates, CarHire, Hotels, Facts, Activities


# Create your views here.
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destinations.objects.all().order_by('name')
    serializer_class = DestinationSerializer


class TourCompaniesViewSet(viewsets.ModelViewSet):
    queryset = TourCompanies.objects.all().order_by('Cname')
    serializer_class = TourCompaniesSerializer


class CarHireViewSet(viewsets.ModelViewSet):
    queryset = CarHire.objects.all().order_by('type')
    serializer_class = CarHireSerializer


class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotels.objects.all().order_by('Hname')
    serializer_class = HotelsSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tourguides.objects.all().order_by('Tname')
    serializer_class = TourguidesSerializer


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all().order_by('desc')
    serializer_class = TripsSerializer


class TweetsViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all().order_by('body')
    serializer_class = TweetsSerializer


class FactsViewSet(viewsets.ModelViewSet):
    queryset = Facts.objects.all().order_by('Fbody')
    serializer_class = FactsSerializer


class updatesViewSet(viewsets.ModelViewSet):
    queryset = updates.objects.all().order_by('body')
    serializer_class = updatesSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all().order_by('name')
    serializer_class = AnimalsSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all().order_by('name')
    serializer_class = ActivitiesSerializer
