from django.test import TestCase
from .views import StoryViewSet
from .models import Story
from rest_framework.test import APITestCase
import json
from django.core import serializers
from .serializers import StorySerializer

class StoryViewSetTest(APITestCase):
    def test_get_story(self):
        request = {'title':'titulo', 'text':'texto'}
        response = self.client.get('/historia/lista_de_historias/', request)
        self.assertEqual(response.status_code, 200)

        request1 = {'title':'titulo'}
        response1 = self.client.post('/historia/lista_de_historias/', request1)
        self.assertEqual(response1.status_code, 400)

    # def test_create_story(self):
    #     request = {'historia':''}
    #     response = self.client.post('/historia/lista_de_historias/', request)
    #     self.assertEqual(response.status_code, 200)