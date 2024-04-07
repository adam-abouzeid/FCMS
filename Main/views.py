from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .util import *

# Create your views here.


def index(request):
    return render(request,"Main/index.html",{
        "News": get_News()
    })