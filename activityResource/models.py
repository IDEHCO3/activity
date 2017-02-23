from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):

    iriObject = models.URLField(blank=False, null=True)
    iriObjectTarget = models.URLField(blank=False, null=True)
    iriAction = models.URLField(blank=False, null=False)
    iriActor = models.URLField(blank=False, null=False)
