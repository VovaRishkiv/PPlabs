from django.test import TestCase
from django.utils import timezone
from rating.models import Rating
# Create your tests here.

class TestRating(TestCase):
    def create_rating(self,group="CS-209", name="Someone", mark=0):
        return Rating.objects.create(group=group, name=name, mark=mark)
   
    def test_create_rating_group(self):
        r = self.create_rating()
        self.assertEqual(r.group, "CS-209")
        
    def test_create_rating_name(self):
        r = self.create_rating()
        self.assertEqual(r.name, "Someone")
        
    def test_create_rating_name(self):
        r = self.create_rating()
        self.assertEqual(r.mark, 0)
        
    def test_create_rating(self):
        r = self.create_rating()
        self.assertTrue(isinstance(r, Rating))