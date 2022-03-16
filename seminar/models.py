from django.db import models
from autoslug import AutoSlugField
from events.models import *
# Create your models here.


class Seminar(models.Model):
    seminar_name = models.CharField(max_length=100)
    seminar_organizer = models.CharField(max_length=100)

    # seminar_date = models.DateField(auto_now=False)
    # organizer_contact_number = models.CharField(max_length=100, blank=True)
    # seminar_address = models.CharField(max_length=200)
    # organizer_contact_email = models.EmailField()
    # seminar_cost = models.CharField(max_length=100, blank=True)
    # seminar_website = models.CharField(max_length=100, blank=True)
    # seminar_style = models.ForeignKey(
    #     Event_style, on_delete=models.CASCADE, null=True, blank=True)
    # competition_type = models.ForeignKey(
    #     Competition_type, on_delete=models.CASCADE, null=True, blank=True)
    # seminar_social_links_fb = models.CharField(max_length=100, blank=True)
    # seminar_social_links_tw = models.CharField(max_length=100, blank=True)
    # organizer_social_links_fb = models.CharField(max_length=100, blank=True)
    # organizer_social_links_tw = models.CharField(max_length=100, blank=True)
    # seminar_rules_regulations = models.TextField(blank=True)
    # special_request_form_seminar_organizer = models.CharField(
    #     max_length=500, blank=True)

    def __str__(self):
        return self.seminar_name
