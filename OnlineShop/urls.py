from django.urls import path

from . import views

urlpatterns = [
      path("FanShop", views.Shop_Main, name="Shop_Main"),

]