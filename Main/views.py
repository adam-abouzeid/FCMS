
from django.shortcuts import render
from .models import *
from .util import *

# Create your views here.


def index(request):

    #STATIC 
    #phrases = ["#We_Are_Leipzig", "#Die_Roten_Bullen","#Follow_RB_LEIPZIG!"]

    return render(request,"Main/index.html",{
        "News": getNews(),
        "user":request.user
    })

def singleNews(request, id):

    singleNews = models.News.objects.get(id=id)

    return render(request,"Main/singleNews.html",{
        "News":singleNews
    })


def news_All(request):
    news = models.News.objects.all()
    return render(request, "Main/All_news.html",{
        "News": news
    })

def OurTeam(request):

    GK = Player.objects.filter(role="GoalKeeper")
    DF = Player.objects.filter(role="Defense")
    MD = Player.objects.filter(role="MiddleFeild")
    FR = Player.objects.filter(role="Forward")
    TR = Player.objects.filter(role="Trainer")

    return render(request, "Main/OurTeam.html", {
        "GK": GK,
        "DF": DF,
        "MD": MD,
        "FR": FR,
        "TR": TR
    })

