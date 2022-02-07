from django.contrib import admin
from django.urls import path, include
from .views import lot, lot_detail, lot_delete
from . import views

urlpatterns = [
        path('index', views.index,name='index'),
        path('index2', views.index2,name='index2'),
        path("", lot, name="lot"),

        path("<int:pk>", lot_detail, name="lot_detail"),
        path("<int:pk>/delete", lot_delete, name="lot_delete")
]
