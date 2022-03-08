from django.db import models
from django.contrib.auth.models import User
import uuid
from events.models import *

# Create your models here.

def unique_upload(instance, filename):
    ext = filename.split('.').pop()
    return "{}.{}".format(uuid.uuid4(), ext)


class UserType(models.Model):
    type = models.CharField(max_length=50)
    

    def __str__(self):
        return self.type

class UserInformation(models.Model):
    type = models.ForeignKey(UserType,on_delete=models.CASCADE, related_name='users_type')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_name')
    age = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    Competition_style = models.CharField(max_length=50)
    Competition_Level = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to = unique_upload)
    # SignedUpEvents = models.ManyToManyField(events)


    def __str__(self): 
        return self.name.username

