
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

def list_fields(request):
    fields = Field.objects.all()
    return render(request, 'Main/list_fields.html', {'fields': fields})




