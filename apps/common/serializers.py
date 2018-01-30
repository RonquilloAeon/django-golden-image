from apps.common.hasher import get_hasher
from rest_framework import serializers


class HashidModelSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()

    def get_pk(self, obj):
        """
        Get hashed pk value
        :param obj: instance to hash pk for
        :return: string
        """
        return get_hasher().encode(obj.pk)
