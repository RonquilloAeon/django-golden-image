from apps.account import models as account_models
from apps.account import serializers
from apps.common.views import get_default_response
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


class AuthenticateViewSet(APIView):
    """
    /api/auth
    """
    permission_classes = (permissions.AllowAny,)
    queryset = account_models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def delete(self, request):
        """
        Delete token to log user out

        :param request: Request object
        :return: Response object
        """
        response = get_default_response('200')

        try:
            authenticated_token = TokenAuthentication().authenticate(request)[1]
            authenticated_token.delete()
        except TypeError:
            response = get_default_response('401')
            response.data['message'] = 'User not logged in'
            response.data['userMessage'] = 'Cannot log out you - you are not logged in!'

        return response

    def post(self, request):
        """
        Log a user in
        :param request: Request object
        :return: Response object
        """
        payload = request.data
        email = payload.get('email')
        password = payload.get('password')
        response = get_default_response('400')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                # User exists and is active, get/create token and return
                if user.is_active:
                    token = Token.objects.get_or_create(user=user)
                    response = get_default_response('201')
                    response.data['token'] = token[0].key
                else:
                    response = get_default_response('403')
                    response.data['message'] = 'User inactive'
                    response.data['userMessage'] = 'Cannot log you in because your user is inactive'
            else:
                response = get_default_response('401')
                response.data['message'] = 'Authentication failed'
                response.data['userMessage'] = 'Email or password incorrect. Please try again.'

        return response


class MeViewSet(generics.RetrieveAPIView):
    """
    /api/me
    Endpoint for retrieving user info
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = account_models.User.objects.all()

    def get(self, request):
        """
        Get user

        :param request: Request object
        :return: Response object
        """
        authenticated_user = TokenAuthentication().authenticate(request)[0]

        response = get_default_response('200')
        response.data['userMessage'] = 'Successfully retrieved your user information!'
        response.data['result'] = serializers.UserSerializer(authenticated_user).data

        return response


class UserViewSet(generics.CreateAPIView):
    """
    /api/user
    Endpoint class for User model
    """
    permission_classes = (permissions.AllowAny,)
    queryset = account_models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def post(self, request):
        """
        Create a new user

        :param request: Request object
        :return: Response object
        """
        payload = request.data
        email = payload.get('email')
        password = payload.get('password')
        request = get_default_response('400')

        if email and password:
            try:
                user = account_models.User.objects.create_user(email, password)

                if user:
                    request = get_default_response('201')
                    request.data['message'] = 'User successfully created'
                    request.data['userMessage'] = 'You have been successfully registered!'
                    request.data['result'] = serializers.UserSerializer(user).data
            except IntegrityError:
                request = get_default_response('409')
                request.data['message'] = 'User already exists'
                request.data['userMessage'] = 'A user with the same email already exists. If you forgot your ' \
                                              'password, you can reset it using the Reset form.'

        return request
