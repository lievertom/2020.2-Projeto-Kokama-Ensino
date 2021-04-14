from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    options = serializers.SlugRelatedField(many=True, read_only=True, slug_field='option')
    class Meta:
        model = Activity
        fields = ['phrase_portuguese', 'phrase_kokama', 'options']