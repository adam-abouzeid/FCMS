
from django.shortcuts import render
from .models import *
from .util import *
from TicketShop.models import Game
# Create your views here.


def index(request):

    recent_games = Game.objects.all().order_by("-date")[:5]  # Get the 5 most recent games
    
    return render(request,"Main/index.html",{
        "News": getNews(),
        "user":request.user,
        "games": recent_games
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

