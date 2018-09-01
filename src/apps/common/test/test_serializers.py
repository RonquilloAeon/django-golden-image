from apps.account.models import User
from apps.common.hasher import get_hasher
from apps.common.serializers import HashidModelSerializer
from django.test import TestCase


class TestUserSerializer(HashidModelSerializer):
    """
    For testing
    """
    class Meta:
        fields = ('pk', 'email')
        model = User


class TestHashidModelSerializer(TestCase):
    def test_hashid_model_serializer_successful(self):
        """
        Test that we can serialize with the hashid serializer
        :return: None
        """
        hasher = get_hasher()
        user = User.objects.create_user(email='test@someemail.com')
        hashed_pk = hasher.encode(user.pk)

        serialized_user_data = TestUserSerializer(user).data

        self.assertEquals(len(serialized_user_data.values()), 2)  # only pk and email
        self.assertEquals(serialized_user_data['email'], user.email)
        self.assertEquals(serialized_user_data['pk'], hashed_pk)
