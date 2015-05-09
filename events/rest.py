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

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return DriversWriteSerializer
        else:
            return self.serializer_class

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return CarsWriteSerializer
        else:
            return self.serializer_class

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

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return EventDriversWriteSerializer
        else:
            return self.serializer_class
