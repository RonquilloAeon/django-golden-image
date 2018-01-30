from apps.account import models as account_models
from apps.common.serializers import HashidModelSerializer


class UserCreateSerializer(HashidModelSerializer):
    class Meta:
        model = account_models.User
        fields = ('pk', 'email', 'password',)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        del validated_data['email']
        del validated_data['password']

        return account_models.User.objects.create_user(email, password, **validated_data)


class UserSerializer(HashidModelSerializer):
    class Meta:
        model = account_models.User
        fields = ('pk', 'email', 'last_login',)
