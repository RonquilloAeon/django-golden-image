from apps.account import models as account_models
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.User
        fields = ('id', 'email', 'password',)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        del validated_data['email']
        del validated_data['password']

        return account_models.User.objects.create_user(email, password, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.User
        fields = ('id', 'email', 'last_login',)
