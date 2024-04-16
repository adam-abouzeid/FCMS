from django.urls import path

from . import views

urlpatterns = [
   path("",views.Community_index,name="Community_index")
]