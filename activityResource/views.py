
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from activityResource.models import Activity
from activityResource.serializers import ActivitySerializer

from activityResource.context import context, addContextInHeader
# Create your views here.

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        response = super(ActivityList, self).get(request, *args, **kwargs)
        url = reverse('activity:context', request=request)
        response = addContextInHeader(url, response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(context, status=200)

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        response = super(ActivityDetail, self).get(request, *args, **kwargs)
        url = reverse('activity:context', request=request)
        response = addContextInHeader(url, response)
        return response

    def options(self, request, *args, **kwargs):
        return Response(context, status=200)

class ActivityContext(APIView):

    def get(self, request, *args, **kwargs):
        return Response(context, status=200)