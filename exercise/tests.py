from django.test import TestCase
from ..views import ActivityViewSet


class ActivityViewSetTest(TestCase):
    def setUp(self) -> None:
        self.phrase = ActivityViewSet(field = 'phrase-kokama')
        self.remover = ActivityViewSet(remove = 'remove')
        self.serializer = ActivityViewSet(many=True, read_only=True, slug_field='option')

    def test_get_data(self):
        url = 'http://api.plos.org/search?q=title:DNA'
        expected = 'banana'
        result = self.test_get_data(url)
        self.assertEqual(expected, result)

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

    
