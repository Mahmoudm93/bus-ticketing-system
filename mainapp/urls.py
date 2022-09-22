from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("book/", views.book, name="book"),
    path("location/", views.location, name="location"),
    path("route/", views.route, name="route"),
    path("assignment/", views.assignment, name="assignment"),
    path("bus/", views.bus, name="bus"), 
    path("view/", views.view, name="view"), 
]