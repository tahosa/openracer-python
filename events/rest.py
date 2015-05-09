from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
from pprint import pprint

from events.models import *
from events.serializers import *

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
