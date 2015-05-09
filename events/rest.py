from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
from pprint import pprint

from events.models import *
from events.serializers import *

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class DriversViewSet(viewsets.ModelViewSet):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class NumbersViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class RunsViewSet(viewsets.ModelViewSet):
    queryset = Runs.objects.all()
    serializer_class = RunsSerializer

class EventDriversViewSet(viewsets.ModelViewSet):
    queryset = EventDrivers.objects.all()
    serializer_class = EventDriversSerializer
