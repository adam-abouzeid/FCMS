from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .util import *

# Create your views here.


def index(request):

    #STATIC 
    #phrases = ["#We_Are_Leipzig", "#Die_Roten_Bullen","#Follow_RB_LEIPZIG!"]

    return render(request,"Main/index.html",{
        "News": get_News(),
    })

def news_card(request, id):

    New = models.News.objects.get(id=id)

    return render(request,"Main/news_card.html",{
        "News":New
    })


def news_All(request):

    return render(request, "Main/All_news.html",{
        "News": get_News(0)
    })




