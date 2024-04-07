from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from Main.models import *

# Create your models here.
# here are the databases that we are going to use for the website


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        FAN = "FAN", 'Fan'
        CLUB_STAFF = "CLUB_STAFF", 'Club_Staff'

    base_role = Role.FAN #since if a fan or club staff needs to register we can handle their registration manually to not be an admin
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    role = models.CharField(max_length=50, choices=Role.choices)
    country = models.CharField(max_length=100)

    

    def save(self, *args, **kwargs):
        # If creating a new user (no primary key yet) !- Updating the user here
        if not self.pk:
            # If it's a superuser being created, set the role to ADMIN
            if self.is_superuser:
                self.role = User.Role.ADMIN
            else:
                # For all other new users, the role is determined by base_role
                self.role = self.base_role
        return super().save(*args, **kwargs)
        
