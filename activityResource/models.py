from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):

    iriActor = models.URLField(blank=False, null=False)
    iriAction = models.URLField(blank=False, null=False)
    iriObject = models.URLField(blank=False, null=True)
    iriObjectTarget = models.URLField(blank=False, null=True)
