from django.test import TestCase
from django.contrib.auth.models import Group, User
from rest_framework.test import APIClient
from django.urls import reverse

from .models import State


def setClient():
    url_get_token = reverse('token_obtain_pair')
    username = 'admin'
    email = 'admin@example.com'
    password = '12345678'

    grpadmin, _ = Group.objects.get_or_create(name='admin')
    user = User.objects.create(
        username=username, email=email
    )
    user.groups.add(grpadmin.id)
    user.set_password(password)
    user.save()

    client = APIClient()
    resp = client.post(
        url_get_token, {'username': username, 'password': password}, 
        format='json'
    )
    token = resp.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    return client


class StateTest(TestCase):
    def setUp(self):
        self.client = setClient()
        self.state = State.objects.create(
            code='PE',
            name='Pernambuco'
        )

    def test_create_state(self):
        response = self.client.post(
            '/api/v1/core/state/',
            data={
                'code': 'PE',
                'name': 'Pernambuco'
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_list_state(self):
        response = self.client.get('/api/v1/core/state/')
        self.assertEqual(response.status_code, 200)

    def test_change_state(self):
        response = self.client.put(
            '/api/v1/core/state/' + str(self.state.id) + '/',
            data={
                'code': 'AL',
                'name': 'Alagoas'
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_state(self):
        response = self.client.delete(
            '/api/v1/core/state/' + str(self.state.id) + '/')
        self.assertEqual(response.status_code, 204)
