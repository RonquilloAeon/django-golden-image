from apps.account import models as account_models
from rest_framework.test import APITestCase


class TestPOST(APITestCase):
    """
    Test /api/me POST (user creation)
    """
    def test_post_successful(self):
        """
        Successful /api/me POST

        :return: None
        """
        # Create user
        payload = {
            'email': 'mrtest@mypapaya.io',
            'password': 'WhoWantsToBeAMillionaire?'
        }

        request = self.client.post('/api/users', data=payload, format='json')
        self.assertEquals(request.status_code, 201)

        user = account_models.User.objects.get(email='mrtest@mypapaya.io')
        self.assertFalse(user.is_superuser)

    def test_post_already_exists(self):
        """
        /api/me POST (user already exists)

        :return: None
        """
        # Create user
        account_models.User.objects.create_user(email='mrtest@mypapaya.io', password='pass')

        # Attempt to create user via API
        payload = {
            'email': 'mrtest@mypapaya.io',
            'password': 'WhoWantsToBeAMillionaire?'
        }

        request = self.client.post('/api/users', data=payload, format='json')
        self.assertEquals(request.status_code, 409)

    def test_post_bad_request(self):
        """
        /api/me POST (bad request)

        :return: None
        """
        # Attempt to create user via API with invalid payload
        request = self.client.post('/api/users', data={'email': 'bad@test.com'}, format='json')
        self.assertEquals(request.status_code, 400)
