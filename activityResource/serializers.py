from rest_framework import serializers
from activityResource.models import Activity
class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'iriActor', 'iriAction', 'iriObject', 'iriObjectTarget')