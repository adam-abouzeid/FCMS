from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Field



def list_fields(request):
    fields = Field.objects.all()
    return render(request, 'list_fields.html', {'fields': fields})