from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name")
    age = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    Competition_style = models.CharField(max_length=50)
    Competition_Level = models.CharField(max_length=50)
    # img = models.ImageField(upload_to=unique_upload)
    # review_page_img = models.ImageField(upload_to=unique_upload)
    about = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    # reviews = models.ManyToManyField(
    #     PlayerReview, related_name="user_reviews", blank=True
    # )

    def __str__(self):
        return self.name