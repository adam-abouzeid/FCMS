
from django.db import models
from django.utils import timezone
from Authentication.models import *

# Create your models here.
# here are the databases that we are going to use for the website

class News(models.Model): # if not specified a primary key is explicitly generated by django migrations
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False)
    category = models.CharField(max_length=50)
    Image = models.TextField(default="https://th.bing.com/th/id/R.daa7359bb5a739976f49f73a13248445?rik=96%2fTS%2buS%2fKFAyA&pid=ImgRaw&r=0")
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title





