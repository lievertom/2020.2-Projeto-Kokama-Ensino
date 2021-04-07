from rest_framework import serializers
from .models import Activity # Contain


# class ContainSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contain
#         fields = ['activity', 'options']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['phrase_portuguese', 'phrase_kokama']