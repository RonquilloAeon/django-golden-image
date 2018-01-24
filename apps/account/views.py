from apps.account import serializers
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthenticateView(APIView):
    """
    /api/auth
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def delete(self, request):
        """
        Delete token to log user out
        :param request: Request object
        :return: Response object
        """
        if not request.user.is_anonymous:
            Token.objects.filter(user=request.user).delete()

        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """
        Log a user in
        :param request: Request object
        :return: Response object
        """
        payload = request.data
        email = payload.get('email')
        password = payload.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                token = Token.objects.get_or_create(user=user)
                return Response(data={'token': token[0].key}, status=status.HTTP_201_CREATED)
            else:
                raise AuthenticationFailed('Email or password incorrect. Please try again.')
        else:
            raise ParseError('email and password fields required')


class MeView(APIView):
    """
    /api/me
    Endpoint for retrieving user info
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Get user
        :param request: Request object
        :return: Response object
        """
        return Response(data=serializers.UserSerializer(request.user).data, status=status.HTTP_200_OK)


class UsersView(generics.CreateAPIView):
    """
    /api/users
    Endpoint class for User model
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSerializer

    def post(self, request, **kwargs):
        """
        Create a new user
        :param request: Request object
        :param kwargs:
        :return: Response object
        """
        payload = request.data
        serializer = serializers.UserCreateSerializer(data=payload)

        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response(data=serializers.UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
