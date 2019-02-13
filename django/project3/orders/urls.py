from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="orders-menu"),
    path("neworder", views.neworder, name="orders-new"),
    path("history", views.orderhistory, name="orders-history"),
    path("contact", views.contactus, name="orders-contact"),
]
