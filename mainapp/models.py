from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.location_name


class Route(models.Model):
    buses1 = [
        ('bus1', 'bus1'),
        ('bus2', 'bus2'),
        ('bus3', 'bus3')
    ]
    route_name = models.CharField(max_length=100, default="")
    bus = models.CharField(max_length=100, choices=buses1, default='bus1')
    distance = models.FloatField(max_length=20, default=0.0)
    fare = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.route_name


class Assignment(models.Model):
    route = models.CharField(max_length=100, default="")
    bus = models.CharField(max_length=100, default="")
    departure_time = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.route


class Bus(models.Model):
    bus_name = models.CharField(max_length=100, default="")
    bus_num = models.IntegerField(max_length=100, default=0)
    from_d = models.CharField(max_length=100, default="")
    to_d = models.CharField(max_length=100, default="")
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    distance = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.bus_name


class BookTicket(models.Model):
    first_name = models.CharField(max_length=200, default="")
    sur_name = models.CharField(max_length=200, default="")
    phone_num = models.IntegerField(default=0)
    email_address = models.EmailField(default="")
    home_address = models.CharField(max_length=200, default="")
    next_kin_name = models.CharField(max_length=200, default="")
    next_kin_phone_num = models.IntegerField(default=0)
    next_kin_home_address = models.CharField(max_length=200, default="")
    # route = models.CharField(max_length=150)
    # complete = models.BooleanField()
    route = models.CharField(max_length=100, default="")
    bus = models.CharField(max_length=200, default="")
    seat_num = models.IntegerField(max_length=100, default=0)
    fare = models.FloatField(max_length=100, default=0.0)
    

    def __str__(self):
        return self.first_name
