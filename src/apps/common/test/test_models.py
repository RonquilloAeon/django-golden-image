from apps.account.models import User
from apps.common.hasher import get_hasher
from apps.common.models import get_uploaded_file_path, HashidManagerMixin
from django.db import models
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


class UserManager(models.Manager, HashidManagerMixin):
    pass


class TestHashidManagerMixin(TestCase):
    class TestUser(User):
        objects = UserManager()

        class Meta:
            app_label = 'account'
            proxy = True

    def test_successful(self):
        """
        Test that we can get an instance by hashid
        :return: None
        """
        hasher = get_hasher()
        user = self.TestUser.objects.create(email='test@test.com')
        hashed_pk = hasher.encode(user.pk)

        retrieved_user = self.TestUser.objects.get_by_hashid(hashed_pk)

        self.assertEquals(retrieved_user, user)

    def test_not_found(self):
        """
        Test that we get default error if model not found
        :return: None
        """
        hasher = get_hasher()
        hashed_pk = hasher.encode(9999)

        with self.assertRaises(self.TestUser.DoesNotExist):
            self.TestUser.objects.get_by_hashid(hashed_pk)
