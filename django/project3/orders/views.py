from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Project 3: TODO")


def menu(request):
    return render(request, 'orders/menu.html', {'title': 'Menu'})


def neworder(request):
    return render(request, 'orders/neworder.html', {'title': 'New Order'})


def orderhistory(request):
    return render(request, 'orders/history.html', {'title': 'Order History'})


def contactus(request):
    return render(request, 'orders/contactus.html', {'title': 'Contact Us'})
