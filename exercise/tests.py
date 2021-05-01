from django.test import TestCase
from .views import ActivityViewSet
from .models import Option, Activity, Contain
from rest_framework.test import APITestCase
import json
from django.core import serializers
from .serializers import ActivitySerializer


class ActivityViewSetTest(APITestCase):
    def test_get_data(self):
        request = {'activity':'fddd','option':'dvfv'}
        response = self.client.get('/historia/atividades/', request)
        self.assertEqual(response.status_code, 200)

    # def test_clean_database(self):
        
    #     request2_2 = Option.objects.create(option='laladk')
    #     request3_2 = Activity.objects.create(phrase_portuguese='porr', phrase_kokama='aaaa')
    #     request3_2.options.set([request2_2])
    #     request1_2 = Contain.objects.create(activity=request3_2, options=request2_2)
       
    #     Contain.objects.all().delete()
    #     variavel = Contain.objects.all()
    #     Option.objects.all().delete()
    #     Activity.objects.all().delete()

    #     self.assertEqual(variavel.exists(), False)
    #     self.assertEqual(Option.objects.all().exists(), False)
    #     self.assertEqual(Activity.objects.all().exists(), False)

    
    # def test__add_possible_options(self):
    #     request_3 = {'options':'lista', 'word':'3', 'option': 'word'}
    #     response_3 = self.client.post('/historia/atividades/', request_3)
    #     self.assertEqual(response_3.status_code, 400)

    
