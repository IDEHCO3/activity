from django.shortcuts import render
from rest_framework import generics
from activityResource.models import Activity
from activityResource.serializers import ActivitySerializer
# Create your views here.

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer