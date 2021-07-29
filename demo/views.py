from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Registration, Login
from django.contrib.auth.models import auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'Home.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST.get('Firstname')
        lastname = request.POST.get('Lastname')
        city = request.POST.get('City')
        state = request.POST.get('State')
        mobile = request.POST.get('Phone')
        zip = request.POST.get('Zip')
        email = request.POST.get('Email')
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        loginobj = Login()
        loginobj.username = username
        loginobj.password = password
        loginobj.save()

        registration = Registration()
        registration.loginid = loginobj
        registration.firstname = firstname
        registration.lastname = lastname
        registration.city = city
        registration.state = state
        registration.mobile = mobile
        registration.zip = zip
        registration.email = email

        registration.save()

        return render(request, 'Home.html')
    return render(request, "register.html")


class Httpresponse:
    pass


def login(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        if Login.objects.filter(username=username, password=password):
            return render(request, 'Home.html')

        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')



