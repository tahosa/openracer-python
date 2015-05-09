from rest_framework import serializers

from events.models import *

class NullSerializerPatch(serializers.BaseSerializer):
    def field_to_native(self, obj, field_name):
        if obj is None:
            return None
        val = getattr(obj, self.source or field_name)
        if val is None:
            return None
        return super(NullSerializerPatch,self).field_to_native(obj, field_name)

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'location', 'name', 'date')

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('id', 'name', 'abbr', 'parent')

class RunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runs
        fields = ('id', 'time', 'cones', 'gates', 'driver')

class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ('id', 'number', 'driver')

class CarsSerializer(serializers.ModelSerializer):
    car_class = ClassesSerializer()

    class Meta:
        model = Cars
        fields = ('id', 'make', 'model', 'year', 'car_class', 'driver_list')

class DriversSerializer(serializers.ModelSerializer, NullSerializerPatch):
    default_car = CarsSerializer(required=False, allow_null=True)
    default_number = NumbersSerializer(required=False, allow_null=True)

    class Meta:
        model = Drivers
        fields = ('id', 'name', 'address', 'emergency_name', 'emergency_phone',
            'novice', 'default_car', 'default_number')

class EventDriversSerializer(serializers.ModelSerializer):
    driver = DriversSerializer()
    car = CarsSerializer()
    number = NumbersSerializer()

    class Meta:
        model = EventDrivers
        fields = ('id', 'event', 'driver', 'car', 'number')

class CarsWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ('id', 'make', 'model', 'year', 'car_class', 'driver_list')

class DriversWriteSerializer(serializers.ModelSerializer, NullSerializerPatch):

    class Meta:
        model = Drivers
        fields = ('id', 'name', 'address', 'emergency_name', 'emergency_phone',
            'novice', 'default_car', 'default_number')

class EventDriversWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventDrivers
        fields = ('id', 'event', 'driver', 'car', 'number')
