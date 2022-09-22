from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookTicket, Location, Route, Assignment, Bus
from .forms import BookATicket, Locations, Routes, Assignments, Busses
# Create your views here.


def index(response, id):
    ls = BookTicket.objects.get(id=id)
    return render(response, "mainapp/base.html", {"ls":ls})


def home(response):
    return render(response, "mainapp/home.html", {})


def view(response):
    return render(response, "mainapp/view.html", {})


def location(response):
    if response.method == "POST":
        form = Locations(response.POST)

        if form.is_valid():
            l = form.cleaned_data["location_name"]
            t = Location(location_name=l)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = Locations()
    return render(response, "mainapp/location.html", {"form":form})


def route(response):
    if response.method == "POST":
        form = Routes(response.POST)

        if form.is_valid():
            r = form.cleaned_data["route_name"]
            b = form.cleaned_data["bus"]
            d = form.cleaned_data["distance"]
            f = form.cleaned_data["fare"]
            t = Route(route_name=r, bus=b, distance=d, fare=f)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = Routes()
    return render(response, "mainapp/route.html", {"form":form})


def assignment(response):
    if response.method == "POST":
        form = Assignments(response.POST)

        if form.is_valid():
            r = form.cleaned_data["route"]
            b = form.cleaned_data["bus"]
            dt = form.cleaned_data["departure_time"]
            t = Assignment(route=r, bus=b, departure_time=dt)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = Assignments()
    return render(response, "mainapp/assignment.html", {"form":form, "assign":assign})


def bus(response):
    if response.method == "POST":
        form = Busses(response.POST)

        if form.is_valid():
            bn = form.cleaned_data["bus_name"]
            bno = form.cleaned_data["bus_num"]
            f = form.cleaned_data["from_d"]
            to = form.cleaned_data["to_d"]
            dt = form.cleaned_data["departure_time"]
            at = form.cleaned_data["arrival_time"]
            d = form.cleaned_data["distance"]
            t = Bus(bus_name=bn, bus_num=bno,
                           from_d=f, to_d=to, departure_time=dt,
                           arrival_time=at, distance=d)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = Busses()
    return render(response, "mainapp/bus.html", {"form":form, "b":b})


def book(response):
    bl = BookTicket.objects.all()
    # assign = Assignment.objects.using('default').all()
    if response.method == "POST":
        form = BookATicket(response.POST)

        if form.is_valid():
            fn = form.cleaned_data["first_name"]
            sn = form.cleaned_data["sur_name"]
            pn = form.cleaned_data["phone_num"]
            ea = form.cleaned_data["email_address"]
            ha = form.cleaned_data["home_address"]
            nkn = form.cleaned_data["next_kin_name"]
            nkpn = form.cleaned_data["next_kin_phone_num"]
            nkha = form.cleaned_data["next_kin_home_address"]
            r = form.cleaned_data["route"]
            # f = form.cleaned_data["fare"]
            # b = form.cleaned_data["bus"]
            # snum = form.cleaned_data["seat_num"]
            t = BookTicket(first_name=fn, sur_name=sn,
                           phone_num=pn, email_address=ea,
                           home_address=ha, next_kin_name=nkn,
                           next_kin_phone_num=nkpn,
                           next_kin_home_address=nkha, route=r)
                           # next_kin_home_address=nkha, route=r, bus=b, fare=f, seat_num=snum)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = BookATicket()
    return render(response, "mainapp/book.html", {"form":form, "bl":bl})


