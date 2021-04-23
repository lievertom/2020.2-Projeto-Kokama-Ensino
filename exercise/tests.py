from django.test import TestCase
from rest_framework.test import APIClient
from .models import Activity, Contain, Option
from story.models import Story

class testUtil(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_pra_dar_ruim(self):
        request = self.client.get('/historia/lista_de_historias') 
        self.assertEquals(200, request.status_code) 
    
    def test_bar(self):
        data = {'text': '20', 'title':'30'}
        request = self.client.post('/historia/lista_de_historias', data, format='json')
        story = Story.objects.last()
        self.assertEquals(data['text'], story.text)


