from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .util import *
from .models import User



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "authentication/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        country = request.POST["country"]



        if(not check_if_country_valid(country)):
            return render(request, "authentication/signup.html", {
                "message": "Please enter a Country"
            })
               

        # Ensure password matches confirmation
        password = request.POST["password"]

        if(not is_strong_password(password)):
            return render(request, "authentication/signup.html", {
                "message": "Password Must be atleast 8 characters long containing atleast one digit, one upercase letter, and one special character"
            })

        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "authentication/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password,country=country)
            user.save()
        except IntegrityError:
            return render(request, "authentication/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "authentication/signup.html")
