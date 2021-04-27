from django.test import TestCase
from .views import ActivityViewSet
from .models import Activity, Contain
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import APIRequestFactory



class ActivityViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.phrase = ActivityViewSet(field = 'phrase-kokama')
        self.remover = ActivityViewSet(remove = 'remove')
        self.serializer = ActivityViewSet(many=True, read_only=True, slug_field='option')

    def test_get_data(self):
        view = UserDetail.as_view()
        request = factory.get('http://192.168.0.15:8001/historia/atividades/')
        response = view(request)
        response.render()
        self.assertEqual(response.content, '{ "phrase_kokama" : "phrase_kokama"}')

    # def test_str_clean_database(self):
    #     phrase = Phrase.objects.create(field = 'phrase-kokama')        
    #     remover = remover.objects.creature(remove = 'remove')
    #     expected = 'kokama'
    #     result = str(self.phrase.remover)
    #     self.assertEqual(expected, result)

    # def test_add_possible_options(self):
    #     phrase = Phrase.objects.create(field = 'phrase-kokama')        
    #     serializer = serializer.objects.creature(many=True, read_only=True, slug_field='option')
    #     expected = 'kokama'
    #     result = str(self.phrase.serializer)
    #     self.assertEqual(expected, result)

    # def test_not_possible_option(self):
    #     phrase = phrase.objects.create('phrase-kokama')        
    #     expected = False
    #     result = str(self.phrase)
    #     self.assertEqual(expected, result)

    
