from django.conf import settings
from hashids import Hashids


class Hasher(Hashids):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def decode_single(self, hashid):
        """
        Decode single hash value
        :param hashid: hashed value
        :return: decoded int
        """
        try:
            return self.decode(hashid)[0]
        except IndexError:
            return None


def get_hasher():
    """
    Return standard hasher
    :return: instance of Hasher
    """
    return Hasher(min_length=8, salt=settings.HASH_SALT)
