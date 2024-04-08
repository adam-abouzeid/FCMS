from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("news",views.news_All,name="news_All"),
   path("news/<int:id>",views.news_card,name="news_card"),
]