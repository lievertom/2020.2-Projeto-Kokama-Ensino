from rest_framework import viewsets, mixins
from django.shortcuts import redirect
import requests
from .models import Activity, Option
from .serializers import ActivitySerializer

import random


def generate_random_exercises(request):
    if request.user.is_superuser:
        response_words = requests.get('https://run.mocky.io/v3/92f3a2e6-1686-454b-9847-5e625bc5959f')
        words = response_words.json()
        #random.shuffle(words)

        for word in words:
            option = Option(option=word['word_kokama'])
            option.save()


        # words = line.split()
        # myword = random.choice(words)
        # option = Option()

        response_phrases = requests.get('https://run.mocky.io/v3/4d176167-1c9c-45af-a74e-679f949cbd0e')
        phrases = response_phrases.json()

        for index, phrase in enumerate(phrases, start=1):
            activity = Activity(phrase_portuguese=phrase['phrase_portuguese'], phrase_kokama=phrase['phrase_kokama'])
            activity.save()

            options_list = random.sample(list(Option.objects.all()), 3)
            for option in options_list:
                activity.options.add(option)
            activity.save()

        return redirect('atividades/')

    else:
        return redirect("admin/login/")



class ActivityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
