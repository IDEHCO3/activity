from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):

    object = models.URLField(blank=False, null=True)
    objectTarget = models.URLField(blank=False, null=True)
    activityType = models.URLField(blank=False, null=False)

    user = models.ForeignKey(User, related_name='activities')