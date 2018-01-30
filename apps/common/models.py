from apps.common.hasher import get_hasher
from django.db import models
import time


class EditMixin(models.Model):
    """
    Abstract class for use in models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HashidManagerMixin(models.Manager):
    def get_by_hashid(self, hashid):
        """
        Get an object by a hashed pk
        :param hashid: hashed pk value
        :return: None
        """
        hasher = get_hasher()

        return self.get(pk=hasher.decode_single(hashid))


def get_uploaded_file_path(instance, filename):
    """
    Function that determines file path for specified file
    :param instance: instance of db object for which file is being saved
    :param filename: name of file
    :return: path to file
    """
    # Seconds since epoch
    current_time = str(round(time.time(), 0)).split('.')[0]

    # Get file extension
    file_pieces = filename.split('.')
    file_extension = file_pieces[len(file_pieces) - 1]

    return 'images/{}.{}'.format(current_time, file_extension)
