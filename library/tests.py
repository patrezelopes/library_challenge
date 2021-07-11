from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime, timezone, timedelta
from .models import Client, Book, RentBook

class BookTestCase(TestCase):
    def setUp(self):
        """
        Setup for the tests
        """
        # Create a user
        username = 'usuario'
        password = 'teste123'
        self.user = User.objects.create_user(
            username=username, password=password
        )

        # User authentication
        self.client = APIClient()
        self.client.login(username=username, password=password)

    def test_create_book(self):
        data = {
            "name": "Harry Potter e a Pedra Filosofal",
            "author": "J.K. Rowling"
        }
        url = reverse('book-list')
        response = self.client.post(url, data=data, format='json')

        # Verifications
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().name, 'Harry Potter e a Pedra Filosofal')


    def test_create_client(self):
        data = {
                "name": "Patreze Lopes"
                }
        url = reverse('client-list')
        response = self.client.post(url, data=data, format='json')

        # Verifications
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.first().name, 'Patreze Lopes')


    def test_create_reserve(self):
        data = {
                "name": "Patreze Lopes"
                }
        url = reverse('client-list')
        self.client.post(url, data=data, format='json')
        data = {
            "name": "Harry Potter e a Pedra Filosofal",
            "author": "J.K. Rowling"
        }
        url = reverse('book-list')
        self.client.post(url, data=data, format='json')

        datetime_late = datetime.now(timezone.utc)-timedelta(days=4)
        data = {
                  "client": str(Client.objects.first().pk),
                  "rented_at": str(datetime_late)
                }
        url = reverse('book-list')
        url += str(Book.objects.first().pk) + '/reserve/'
        response = self.client.post(url, data=data, format='json')

        # Verifications
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RentBook.objects.count(), 1)
        self.assertEqual(RentBook.objects.first().rented_at.day, (datetime_late).day)
        self.assertEqual(float(RentBook.objects.first().finerate()), 0.066) #4 day late. fine = 5% and rate = 0.4%*4 = 0.066



