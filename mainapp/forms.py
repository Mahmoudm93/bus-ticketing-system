from django import forms


class BookATicket(forms.Form):
    # name = forms.CharField(label="Name", max_length=200)
    first_name = forms.CharField(label="First Name", max_length=200)
    sur_name = forms.CharField(label="Surname", max_length=200)
    phone_num = forms.IntegerField(label="Phone Number")
    email_address = forms.EmailField(label="Email address")
    home_address = forms.CharField(label="Home Address", max_length=200)
    next_kin_name = forms.CharField(label="Next of Kin Name", max_length=200)
    next_kin_phone_num = forms.IntegerField(label="Next of Kin Phone Number")
    next_kin_home_address = forms.CharField(label="Next of Kin Address", max_length=200)
    route = forms.CharField(label="Route", max_length="100")
    # check = forms.BooleanField(required=False)
    # route =forms.CharField(label="Route", max_length=200)


class Locations(forms.Form):
    location_name = forms.CharField(label="Location Name")


class Routes(forms.Form):
    route_name = forms.CharField(label="Route Name")
    bus = forms.CharField(label="Bus")
    distance = forms.FloatField(label="Distance")
    fare = forms.FloatField(label="Fare")


class Assignments(forms.Form):
    route = forms.CharField(label="Route")
    bus = forms.CharField(label="Bus")
    departure_time = forms.CharField(label="Departure Time")


class Busses(forms.Form):
    bus_name = forms.CharField(label="Bus Name")
    bus_num = forms.IntegerField(label="Bus Number")
    from_d = forms.CharField(label="From (Destination)")
    to_d = forms.CharField(label="To (Destination)")
    departure_time = forms.TimeField(label="Departure Time")
    arrival_time = forms.TimeField(label="Arrival Time")
    distance = forms.FloatField(label="Distance")