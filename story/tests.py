from django.test import TestCase
from django.apps import apps
from .models import Story
from .apps import StoryConfig


class StoryModelTest(TestCase):

    def setUp(self):
        Story.objects.create(title='test_title', text='test_text')

    def test_story_str(self):
        story = Story.objects.get(title='test_title')
        self.assertEqual(str(story), 'test_title')

class StoryConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(StoryConfig.name, 'story')
        self.assertEqual(apps.get_app_config('story').name, 'story')