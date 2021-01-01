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


class GRPCTest(TestCase):
    def test_token(self):
        import grpc
        import microservices_Auth_pb2
        import microservices_Auth_pb2_grpc
        invalid_token = ""
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = microservices_Auth_pb2_grpc.AccessControlStub(channel)
            ans = stub.Retrieve(microservices_Auth_pb2.AccessRequest(token=invalid_token, targetEndpoint="/list",
                                                                     microServiceName="test"))
            print(ans)
