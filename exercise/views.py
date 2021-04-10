from rest_framework import viewsets, mixins
from django.shortcuts import redirect
import requests
from .models import Activity, Option, Contain;
from .serializers import ActivitySerializer

import random

def clean_database():
    Contain.objects.all().delete()
    Option.objects.all().delete()
    Activity.objects.all().delete()



def generate_random_exercises(request):
    clean_database()
    if request.user.is_superuser:
        response_phrases = requests.get('https://run.mocky.io/v3/4d176167-1c9c-45af-a74e-679f949cbd0e')
        phrases = response_phrases.json()

        remove_chars = set([',', '.', '<', '>'])

        for phrase in phrases:
            activity = Activity(phrase_portuguese=phrase['phrase_portuguese'], phrase_kokama=phrase['phrase_kokama'])
            activity.save()

            options_list = phrase['phrase_kokama'].split()
            options = []
            for untreated_option in options_list:
                word = ''.join([c for c in untreated_option if c not in remove_chars])
                option = Option(option=word.lower())
                options.append(option)
                if option not in Option.objects.all():
                    option.save()
            
            correct_word = random.choice(options)
            correct_option = Option.objects.filter(option=correct_word)[0]
            activity.options.add(correct_option)

        for phrase in phrases:
            activity = Activity.objects.filter(phrase_kokama=phrase['phrase_kokama'])[0]
            phrase_words = []
            for untreated_word in activity.phrase_kokama:
                phrase_words.append(''.join([c for c in untreated_word if c not in remove_chars]))

            options_list = random.sample(list(Option.objects.all()), 3)
            repeat = True
            while repeat:
                for option in options_list:
                    if(option.option in phrase_words or activity.options.all()[0] in options_list):
                        options_list = random.sample(list(Option.objects.all()), 3)
                        repeat = True
                        break
                    else:
                        repeat = False
    
            for option in options_list:
                activity.options.add(option)
            activity.save()

        return redirect('atividades/')

    else:
        return redirect("admin/login/")



class ActivityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
