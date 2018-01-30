from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Rental, Comment

# Create your tests here.

class RentalModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rental.objects.create(title='A new title',
                            description='A super cool description',
                            rent=10,
                            location='Pokhara, Nepal',
                            )

    def setUp(self):
        pass

    def test_rental_fields(self):
        obj = Rental.objects.get(pk=1)
        self.assertEqual(obj.title, 'A new title')
        self.assertEqual(obj.description, "A super cool description")
        self.assertEqual(obj.rent, 10)
        self.assertEqual(obj.location, 'Pokhara, Nepal')

    def test_title_label(self):
        title = Rental.objects.get(id=1)
        field_label = title._meta.get._field('title').verbose_name
        self.assertEquals(field_label, 'title')




