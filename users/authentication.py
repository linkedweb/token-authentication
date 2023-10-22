from django.conf import settings

from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get(settings.AUTH_COOKIE)

        if not token:
            return None

        return self.authenticate_credentials(token)
