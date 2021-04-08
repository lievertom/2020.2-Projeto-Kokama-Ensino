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

        response_phrases = requests.get('https://run.mocky.io/v3/4d176167-1c9c-45af-a74e-679f949cbd0e')
        phrases = response_phrases.json()

        remove_chars = set([',', '.', '<', '>'])

        for phrase in phrases:
            # A atvidade
            # A opção certa
            # 3 opções aleatórias
            activity = Activity(phrase_portuguese=phrase['phrase_portuguese'], phrase_kokama=phrase['phrase_kokama'])
            activity.save()

            options_list = phrase['phrase_kokama'].split()
            options = []
            for untreated_option in options_list:
                word = ''.join([c for c in untreated_option if c not in remove_chars])
                option = Option(option=word)
                options.append(option)
                option.save()
            
            correct_word = random.choice(options)
            correct_option = Option.objects.filter(option=correct_word)[0]
            activity.options.add(correct_option)

        for phrase in phrases:
            activity = Activity.objects.filter(phrase_kokama=phrase['phrase_kokama'])[0]
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
