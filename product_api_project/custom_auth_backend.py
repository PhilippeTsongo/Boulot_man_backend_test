from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions

class SimpleKWTAuthentication(JWTAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = request.headers.get('Authorization', '').split()
        if not auth or auth[0].lower() != self.keyword.lower():
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed('Invalid Authorization header. No credentials provided.')
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed('Invalid Authorization header. Token string should not contain spaces.')

        return super().authenticate(request)
