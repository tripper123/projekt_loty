from django.contrib import admin
from django.urls import path, include
from .views import lot, lot_detail, lot_delete, dodaj_lot, detail, index, pagination, usun_lot, user_login, index3
from . import views

urlpatterns = [
        path("lot", views.PostListView.as_view(), name="lot"),
        path("lot.id", lot_detail, name="lot_detail"),
        path("<int:pk>", lot_detail, name="lot_detail"),
        path("<int:pk>/delete", lot_delete, name="lot_delete"),
        path(" dodaj_lot ", dodaj_lot, name="dodaj_lot"),
        path("", index, name="index"),
        path("pagination", index, name="pagination"),
        path("     ", views.PostListView.as_view(), name= "lot"),
        path(" detail ", views.PostListView2.as_view(), name= "detail"),
        path(" usun_lot ", views.PostListView3.as_view(), name= "usun_lot"),
        path("login/", views.user_login, name="login"),
        path("        ", index3, name="index3"),

]
