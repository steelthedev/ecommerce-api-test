from django.test import TestCase
from .models import Product
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase




class TestProducModel(TestCase):

    def get_object(self):
        return Product.objects.create(
            name="test",
            price=float(2000),
        )
        
        
    def test_model(self):
        self.assertTrue(isinstance(self.get_object(),Product))
       
