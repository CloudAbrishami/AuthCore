import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


# initialize the APIClient app

class UserTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.invalid_user = {
            "username": "mahdi",
            "role": "1"
        }
        self.valid_user = {
            "username": "mahdi",
            "password": "123ASD#!@jooon",
            "role": "1"
        }
        self.weekPass_user = {
            "username": "mahdi",
            "password": "123",
            "role": "2"
        }

    def test_create_invalid_user(self):
        response = self.client.post(
            reverse('register'),
            data=json.dumps(self.invalid_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_user(self):
        response = self.client.post(
            reverse('register'),
            data=json.dumps(self.valid_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
