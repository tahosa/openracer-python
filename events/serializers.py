from rest_framework import serializers

from events.models import *


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'location', 'name', 'date')

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ('id', 'name', 'address', 'emergency_name', 'emergency_phone',
            'novice', 'default_car', 'default_number')

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'make', 'model', 'year', 'car_class', 'driver_list')

class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ('id', 'number', 'driver')

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('id', 'name', 'parent')

class RunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runs
        fields = ('id', 'time', 'cones', 'gates', 'driver')

class EventDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDrivers
        fields = ('id', 'event', 'driver', 'car', 'number')
