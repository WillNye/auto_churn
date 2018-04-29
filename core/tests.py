from django.urls import reverse
from rest_framework.test import APITestCase

"""
To run test
python manage.py test --settings=cookify.settings.testing -k
"""


class AuthenticatedTestCase(APITestCase):

    def setUp(self):
        self.as_manager()
        self.contact_id = 676

    def as_manager(self):
        get_token_url = reverse('get_auth_token')
        user_credentials = {'username': '', 'password': ''}
        user_token = self.client.post(get_token_url, data=user_credentials, format='json')
        user_token = user_token.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token)

    def as_base_employee(self):
        get_token_url = reverse('get_auth_token')
        user_credentials = {'username': '', 'password': ''}
        user_token = self.client.post(get_token_url, data=user_credentials, format='json')
        user_token = user_token.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token)

    def as_contact(self):
        get_token_url = reverse('get_auth_token')
        user_credentials = {'username': '', 'password': ''}
        user_token = self.client.post(get_token_url, data=user_credentials, format='json')
        user_token = user_token.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token)


