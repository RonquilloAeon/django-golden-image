from rest_framework.authtoken.models import Token


def get_token_for_user(user):
    """
    Create/get a token for a user. Simulates authentication.

    :param user: Usr object
    :return: token
    """
    token = Token.objects.get_or_create(user=user)
    return token[0].key
