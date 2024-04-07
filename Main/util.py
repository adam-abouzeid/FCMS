import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from . import models

def get_News():
    """
    return a list of atleast the latest five news
    """
    news = models.News.objects.order_by("-date_uploaded")[:5]
    return news