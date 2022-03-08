from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import uuid
import os

# Create your models here.


def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return "user_{0}/{1}".format(instance.id, filename)


def unique_upload(instance, filename):
    ext = filename.split(".").pop()
    return "{}.{}".format(uuid.uuid4(), ext)


def unique_upload_events(instance, filename):
    ext = filename.split(".").pop()
    return "events/{}.{}".format(uuid.uuid4(), ext)


class PlayerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    rating = models.IntegerField(default=0, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]


class Player(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name")
    age = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    Competition_style = models.CharField(max_length=50)
    Competition_Level = models.CharField(max_length=50)
    img = models.ImageField(upload_to=unique_upload)
    review_page_img = models.ImageField(upload_to=unique_upload)
    about = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    reviews = models.ManyToManyField(
        PlayerReview, related_name="user_reviews", blank=True
    )

    def __str__(self):
        return self.name

    @property
    def player_link(self):
        return reverse("review_page", kwargs={"slug": self.slug})

    @property
    def num_5star(self):
        return self.reviews.filter(rating=5).count()

    @property
    def num_4star(self):
        return self.reviews.filter(rating=4).count()

    @property
    def num_3star(self):
        return self.reviews.filter(rating=3).count()

    @property
    def num_2star(self):
        return self.reviews.filter(rating=2).count()

    @property
    def num_1star(self):
        return self.reviews.filter(rating=1).count()


class location(models.Model):
    location_Title = models.CharField(max_length=50)
    latitude = models.FloatField(max_length=15)
    longitude = models.FloatField(max_length=15)

    def __str__(self):
        return self.location_Title


class Event_style(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class Competition_type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_organizer = models.CharField(max_length=100)
    event_date = models.DateField(auto_now=False)
    organizer_contact_number = models.CharField(max_length=100, blank=True)
    event_address = models.CharField(max_length=200)
    organizer_contact_email = models.EmailField()
    event_cost = models.CharField(max_length=100, blank=True)
    event_website = models.CharField(max_length=100, blank=True)
    event_style = models.ForeignKey(
        Event_style, on_delete=models.CASCADE,null=True, blank=True)
    competition_type = models.ForeignKey(
        Competition_type, on_delete=models.CASCADE,null=True, blank=True)
    event_social_links_fb = models.CharField(max_length=100, blank=True)
    event_social_links_tw = models.CharField(max_length=100, blank=True)
    organizer_social_links_fb = models.CharField(max_length=100, blank=True)
    organizer_social_links_tw = models.CharField(max_length=100, blank=True)
    event_rules_requlations = models.TextField(blank=True)
    special_request_form_event_organizer = models.CharField(
        max_length=500, blank=True)

    def __str__(self):
        return self.event_name


class Event(models.Model):
    title = models.CharField(max_length=100)
    event_Location = models.OneToOneField(location, on_delete=models.CASCADE)
    eventType = models.CharField(max_length=50)
    img = models.ImageField(upload_to=unique_upload_events)
    player_1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="players_1"
    )
    player_2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="players_2"
    )
    date = models.DateField(auto_now_add=False, blank=True)
    time = models.TimeField(blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title")
    news_type = models.CharField(max_length=50)
    news_discription = models.CharField(max_length=500)
    # content = models.TextField(max_length=5000)
    content = RichTextUploadingField(blank=True, null=True)
    img = models.ImageField(upload_to=unique_upload_events)
    # date = models.DateField(auto_now_add=False, blank=True)
    # time = models.TimeField(blank=True)
    date_time = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def news_link(self):
        return reverse("news_page", kwargs={"slug": self.slug})

    # def get_absolute_url(self):
    #     return reverse('blog')
