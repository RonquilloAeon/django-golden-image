from apps.account import models as account_models
from apps.common.test import helpers as test_helpers
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from unittest import skip


class TestDELETE(APITestCase):
    def test_delete_successful(self):
        """
        Test that we can log a user out

        :return: None
        """
        # Create a user
        user = account_models.User.objects.create_user(email='test@test.com')

        # Simulate auth
        token = test_helpers.get_token_for_user(user)

        # Get data from endpoint
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        request = self.client.delete('/api/auth')

        self.assertEquals(request.status_code, 200)

        tokens = Token.objects.all()

        self.assertEquals(len(tokens), 0)

    def test_delete_user_not_authenticated(self):
        """
        Test that we get a HTTP 401 status code if user not logged in

        :return: None
        """
        # Get data from endpoint
        request = self.client.delete('/api/auth')
        self.assertEquals(request.status_code, 401)


class TestPOST(APITestCase):
    """
    Test endpoint to log user in
    """
    def test_post_successful(self):
        """
        /api/auth POST

        :return: None
        """
        # Create user
        account_models.User.objects.create_user(email='mrtest@mypapaya.io', password='WhoWantsToBeAMillionaire?')

        # Log user in
        payload = {
            'email': 'mrtest@mypapaya.io',
            'password': 'WhoWantsToBeAMillionaire?'
        }

        request = self.client.post('/api/auth', data=payload, format='json')
        response = request.data

        self.assertIsNotNone(response['token'])

    def test_post_bad_request(self):
        """
        Test that we get a HTTP 400 code if email and/or password missing in payload

        :return: None
        """
        # Create user
        account_models.User.objects.create_user(email='mrtest@mypapaya.io', password='WhoWantsToBeAMillionaire?')

        # Log user in
        payload = {
            'email': 'mrtest@mypapaya.io',
        }

        request = self.client.post('/api/auth', data=payload, format='json')
        self.assertEquals(request.status_code, 400)

    @skip('Cannot deactivate user for some reason')
    def test_post_inactive_user(self):
        """
        Test that we get a HTTP 403 if user is not active

        :return: None
        """
        # Create user
        user = account_models.User.objects.create_user(email='mrtest@mypapaya.io', password='WhoWantsToBeAMillionaire?')
        user.is_active = False
        user.save()

        # Log user in
        payload = {
            'email': 'mrtest@mypapaya.io',
            'password': 'WhoWantsToBeAMillionaire?'
        }

        request = self.client.post('/api/auth', data=payload, format='json')
        self.assertEquals(request.status_code, 403)

    def test_post_incorrect_credentials(self):
        """
        Verify that we get a HTTP 401 code if authentication fails

        :return: None
        """
        # Create user
        account_models.User.objects.create_user(email='mrtest@mypapaya.io', password='WhoWantsToBeAMillionaire?')

        # Log user in
        payload = {
            'email': 'mrtest@mypapaya.io',
            'password': 'Me!'
        }

        request = self.client.post('/api/auth', data=payload, format='json')
        self.assertEquals(request.status_code, 401)

    def test_post_does_not_exist(self):
        """
        Verify that we get a HTTP 401 code if user does not exist

        :return: None
        """
        payload = {
            'email': 'mrtest@mypapaya.io',
            'password': 'Me!'
        }

        request = self.client.post('/api/auth', data=payload, format='json')
        self.assertEquals(request.status_code, 401)
