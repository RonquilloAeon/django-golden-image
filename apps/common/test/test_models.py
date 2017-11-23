from apps.account.models import User
from apps.common.models import get_uploaded_file_path
from django.test import TestCase


class TestGetUploadedFilePath(TestCase):
    def test_successful(self):
        """
        Test that the correct file path is created for an instance that isn't recipe or user

        :return: None
        """
        user = User.objects.create_user('m@mypapaya.io', 'papaya')
        path = get_uploaded_file_path(user, 'apps/common/test/images/avatar-1.png')

        self.assertRegex(path, '^images\/\d+\.\w{3,4}$')
