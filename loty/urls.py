from django.contrib import admin
from django.urls import path, include
from .views import lot, lot_detail, lot_delete, dodaj_lot
from . import views

urlpatterns = [

        path("", lot, name="lot"),
        path("lot.id", lot_detail, name="lot_detail"),
        path("<int:pk>", lot_detail, name="lot_detail"),
        path("<int:pk>/delete", lot_delete, name="lot_delete"),
        path(" ", dodaj_lot, name="dodaj_lot"),

]
