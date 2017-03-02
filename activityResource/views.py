
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from activityResource.models import Activity
from activityResource.serializers import ActivitySerializer

from activityResource.context import context
# Create your views here.

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def options(self, request, *args, **kwargs):
        return Response(context, status=200)

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def options(self, request, *args, **kwargs):
        return Response(context, status=200)

class ActivityContext(APIView):

    def get(self, request, *args, **kwargs):
        return Response(context, status=200)