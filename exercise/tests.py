from django.test import TestCase
from django.apps import apps
from .models import Activity, Option, Contain
from .apps import ExerciseConfig

# Models

class ActivityModelTest(TestCase):
    def setUp(self):
        activity = Activity.objects.create(
            phrase_kokama='Kokama phrase',
            phrase_portuguese='Portuguese phrase'
        )
        option = Option.objects.create(option='test_option')
        activity.options.set(4*[option])
        activity.save()
        
    def test_activity_str(self):
        activity = Activity.objects.get(phrase_kokama='Kokama phrase')
        self.assertEqual(str(activity), 'Kokama phrase')


class OptionModelTest(TestCase):
    def setUp(self):
        option = Option.objects.create(option='test_option')
        
    def test_option_str(self):
        option = Option.objects.get(option='test_option')
        self.assertEqual(str(option), 'test_option')


class ContainModelTest(TestCase):
    def setUp(self):
        activity = Activity.objects.create(
            phrase_kokama='Kokama phrase',
            phrase_portuguese='Portuguese phrase'
        )
        option = Option.objects.create(option='test_option')
        activity.options.set(4*[option])
        activity.save()

        Contain.objects.create(activity=activity, options=option)
        
    def test_contain_str(self):
        activity = Activity.objects.get(phrase_kokama='Kokama phrase')
        option = Option.objects.get(option='test_option')
        contain = Contain.objects.filter(activity=activity, options=option).first()
        self.assertEqual(str(contain), 'Kokama phrase <-> test_option')


# Apps

class ExerciseConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(ExerciseConfig.name, 'exercise')
        self.assertEqual(apps.get_app_config('exercise').name, 'exercise')