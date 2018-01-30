from apps.common import hasher
from django.test import TestCase


class TestHasher(TestCase):
    def test_hasher_successful(self):
        """
        Test that we can encode and decode an integer value
        :return: None
        """
        h = hasher.get_hasher()
        pk_value = 29303

        hashed = h.encode(pk_value)

        self.assertIsInstance(hashed, str)

        self.assertEquals(h.decode_single(hashed), pk_value)

    def test_hasher_bad_hashid(self):
        """
        Test that we get none if hashid is bad
        :return: None
        """
        h = hasher.get_hasher()

        self.assertIsNone(h.decode_single('eeses'))
