from rest_framework import viewsets, mixins
from django.shortcuts import redirect
import requests
from .models import Activity, Option, Contain;
from .serializers import ActivitySerializer
from django.views.decorators.http import require_http_methods

import random

class ActivityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    remove_chars = set([',', '.', '<', '>'])

    def _get_data(self):
        url = 'https://run.mocky.io/v3/4d176167-1c9c-45af-a74e-679f949cbd0e'
        api_request = requests.get(url)
        try:
            api_request.raise_for_status()
            return api_request.json()
        except BaseException as e:
            print("\n\nOcorreu um erro na requisição\n\n")
            raise e
            return None
        except:
            return None


    def _clean_database(self):
        Contain.objects.all().delete()
        Option.objects.all().delete()
        Activity.objects.all().delete()


    def _add_possible_options(self, kokama_phrase):
        options = []
        for untreated_option in kokama_phrase.split():
            word = ''.join([c for c in untreated_option if c not in self.remove_chars])
            option = Option(option=word.lower())
            options.append(option)
            if option not in Option.objects.all():
                option.save()
        
        return options


    def generate_random_exercises(self):
        print("\n\nNew GET Request and database update...\n\n")
        phrases = self._get_data()
        self._clean_database()

        for phrase in phrases:
            activity = Activity(phrase_portuguese=phrase['phrase_portuguese'], phrase_kokama=phrase['phrase_kokama'])
            activity.save()

            options = self._add_possible_options(phrase['phrase_kokama'])
            
            correct_option_word = random.choice(options)
            correct_option = Option.objects.filter(option=correct_option_word)[0]
            activity.options.add(correct_option)

        for phrase in phrases:
            activity = Activity.objects.filter(phrase_portuguese=phrase['phrase_portuguese'], phrase_kokama=phrase['phrase_kokama'])[0]
            phrase_words = []
            for untreated_word in activity.phrase_kokama.split():
                phrase_words.append(''.join([c for c in untreated_word if c not in self.remove_chars]))

            correct_option = activity.options.all()[0]
            options_list1 = Option.objects.exclude(option=correct_option)
            options_list2 = options_list1.exclude(option__in=phrase_words)
            options_list3 = random.sample(list(options_list2), 3)
    
            for option in options_list3:
                activity.options.add(option)
            activity.save()

        return redirect('atividades/')