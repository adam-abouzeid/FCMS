
from django.shortcuts import render, redirect
from .models import *
from .util import *
from django.contrib.auth.decorators import login_required
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

@login_required
def book_field(request, field_id):
    
    field = Field.objects.get(id=field_id)

    if request.method == 'POST':
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        
        existing_bookings = Booking.objects.filter(
            field=field,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
            
        if existing_bookings.exists():
            new_booking = Booking(user=request.user, field=field, date=date, start_time=start_time, end_time=end_time)
                
            new_booking.save()
                
            new_booking.delete()
            message = 'Your booking conflicts with an existing booking and has been cancelled.'
            return render(request, 'Main/booking_error.html', {'error_message': message, 'field': field})
            
        booking = Booking(user=request.user, field=field, date=date, start_time=start_time, end_time=end_time)
        booking.save()
            
        return redirect('list_fields')
        

    return render(request, 'Main/book_field.html', {'field': field})

