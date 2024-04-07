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

    base_role = Role.ADMIN #since if a fan or club staff needs to register we can handle their registration manually to not be an admin
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    
    role = models.CharField(max_length=50, choices=Role.choices)
    country = models.CharField(max_length=100)

    

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg,**kwargs)
        
        
class FanManager(BaseUserManager): #filter only fans when you query data
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.FAN)

        
class Fan(User): #this is a proxy model it wont be generated it justs makes the process of seperation easier

    base_role = User.Role.FAN
    fan = FanManager()

    class Meta:
        proxy = True

@receiver(post_save, sender=Fan)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "FAN":
        FanProfile.objects.create(user=instance)


        
class FanProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fan_id = models.IntegerField(null=True, blank=True)


class ClubStaffManager(BaseUserManager): #filter only club staff when you query data
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.CLUB_STAFF)

        
class Club_Staff(User): #this is a proxy model it wont be generated it justs makes the process of seperation easier

    base_role = User.Role.CLUB_STAFF
    club_staff = ClubStaffManager()

    class Meta:
        proxy = True

@receiver(post_save, sender=Club_Staff)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUB_STAFF":
        Club_Staff_Profile.objects.create(user=instance)


        
class Club_Staff_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    club_staff_id = models.IntegerField(null=True, blank=True)


    
    


#Note that roles cannot be transitioned from one role to another, if someone has more than one role multiple instances must be present in each group role 
