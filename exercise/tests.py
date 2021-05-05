from django.test import TestCase
from django.apps import apps
from .models import Activity, Option, Contain
from .apps import ExerciseConfig
from .views import ActivityViewSet
import requests
from decouple import config


KOKAMA_PHRASE = 'Kokama phrase'
# Models

class ActivityModelTest(TestCase):
    def setUp(self):
        activity = Activity.objects.create(
            phrase_kokama=KOKAMA_PHRASE,
            phrase_portuguese='Portuguese phrase'
        )
        option = Option.objects.create(option='test_option')
        activity.options.set(4*[option])
        activity.save()
        
    def test_activity_str(self):
        activity = Activity.objects.get(phrase_kokama=KOKAMA_PHRASE)
        self.assertEqual(str(activity), KOKAMA_PHRASE)


class OptionModelTest(TestCase):
    def setUp(self):
        Option.objects.create(option='test_option')
        
    def test_option_str(self):
        option = Option.objects.get(option='test_option')
        self.assertEqual(str(option), 'test_option')


class ContainModelTest(TestCase):
    def setUp(self):
        activity = Activity.objects.create(
            phrase_kokama=KOKAMA_PHRASE,
            phrase_portuguese='Portuguese phrase'
        )
        option = Option.objects.create(option='test_option')
        activity.options.set(4*[option])
        activity.save()

        Contain.objects.create(activity=activity, options=option)
        
    def test_contain_str(self):
        activity = Activity.objects.get(phrase_kokama=KOKAMA_PHRASE)
        option = Option.objects.get(option='test_option')
        contain = Contain.objects.filter(activity=activity, options=option).first()
        self.assertEqual(str(contain), KOKAMA_PHRASE + ' <-> test_option')


# Apps

class ExerciseConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(ExerciseConfig.name, 'exercise')
        self.assertEqual(apps.get_app_config('exercise').name, 'exercise')

    
# Views

class ActivityViewSetTest(TestCase):
        
    remove_chars = set([',', '.', '<', '>'])

    def test_get_data(self):
        correct_url = '{base_url}/{parameter}'.format(base_url = config('TRANSLATE_MICROSERVICE_URL'), parameter = 'frases/')
        response = ActivityViewSet.get_data(self, correct_url)
        self.assertEqual(response.status_code, 200)

        response = ActivityViewSet.get_data(self, 'wrong_url')
        self.assertEqual(response.status_code, 500)

    def test_add_possible_options(self):
        kokama_phrase = 'I, love, panara <a lot>.'
        expected = ['I', 'love', 'panara', 'a', 'lot']
        options = ActivityViewSet.add_possible_options(self, kokama_phrase)
        result = []
        for option in options:
            result.append(str(option))
        self.assertEqual(result, expected)
