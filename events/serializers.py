from rest_framework import serializers

from events.models import *


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'location', 'name', 'date')
