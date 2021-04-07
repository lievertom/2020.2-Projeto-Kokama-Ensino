from rest_framework import viewsets, mixins
from django.shortcuts import render
import requests
from .models import Activity #Contain
from .serializers import ActivitySerializer # ContainSerializer


#def home(request):
    # response_words = requests.get('https://run.mocky.io/v3/92f3a2e6-1686-454b-9847-5e625bc5959f')
    # words = response_words.json()

    # response_phrases = requests.get('https://run.mocky.io/v3/4d176167-1c9c-45af-a74e-679f949cbd0e')
    # phrases = response_phrases.json()

    # return render(request, 'home.html', {'words': words, 'phrases': phrases})


# class ContainViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Contain.objects.all()
#     serializer_class = ContainSerializer


class ActivityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer