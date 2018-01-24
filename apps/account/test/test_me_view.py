from apps.account import models as account_models
from apps.common.test import helpers as test_helpers
from rest_framework.test import APITestCase


class TestGET(APITestCase):
    """
    Test /api/me
    """
    def test_get_successful(self):
        """
        Successful /api/me GET
        :return: None
        """
        # Create data
        user = account_models.User.objects.create_user(email='test@test.com')

        # Simulate auth
        token = test_helpers.get_token_for_user(user)

        # Get data from endpoint
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        request = self.client.get('/api/me')
        result = request.data

        self.assertEquals(result['email'], user.email)
