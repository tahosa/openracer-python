from django.db import models

# Create your models here.
class Drivers(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=False)
    emergency_name = models.CharField(max_length=100, blank=False)
    emergency_phone = models.CharField(max_length=10, blank=False)
    novice = models.BooleanField(default=True)
    default_car = models.ForeignKey('Cars')
    default_number = models.ForeignKey('Numbers')

    def __str__(self):
        return self.name

class Cars(models.Model):
    make = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=200, blank=False)
    year = models.CharField(max_length=4)
    car_class = models.ForeignKey('Classes')

    def __str_(self):
        return "{0} {1} {2} ({3})".format(self.year, self.make, self.model, self.car_class.name)

class Numbers(models.Model):
    number = models.IntegerField(blank=False)

    def __str__self():
        return str(self.number);

class Events(models.Model):
    location = models.CharField(max_length=200, blank=False)
    name = models.CharField(max_length=200, blank=False)
    date = models.DateField()

    def __str_(self):
        return "{0} ({1})".format(self.name, self.date)

class Runs(models.Model):
    time = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    cones = models.IntegerField()
    gates = models.IntegerField()
    driver = models.ForeignKey('EventDrivers')

class Classes(models.Model):
    name = models.CharField(max_length=20, blank=False)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __str_(self):
        return self.name

class EventDrivers(models.Model):
    event = models.ForeignKey('Events')
    driver = models.ForeignKey('Drivers')
    car = models.ForeignKey('Cars')
    number = models.ForeignKey('Numbers')

    def __str_(self):
        return "{0} - {1}".format(self.number.number, self.driver.name)
