from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='fields/',default='fields/default.jpg')

    def __str__(self):
        return self.name



# Create your models here.
