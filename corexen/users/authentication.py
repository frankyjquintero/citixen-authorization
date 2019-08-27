from django.utils.translation import ugettext_lazy as _
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed


class CitixenAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            #slug_id = api_settings.USER_ID_CLAIM
            user_uuid = validated_token['uuid']
        except KeyError:
            raise InvalidToken(_('Token contained no recognizable user identification'))
        user = None  # Get user info
        return user
