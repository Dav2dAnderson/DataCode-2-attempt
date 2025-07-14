from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework import status

from .models import BlacklistedAccessToken


class BlacklistAccessTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):

        EXEMPT_PATHS = [
            '/api/main_space/',
        ]

        for path in EXEMPT_PATHS:
            if request.path.startswith(path):
              return None

        headers = request.headers.get('Authorization', '')
        if headers.startswith('Bearer '):
            token = headers.split(' ')[1]
            if BlacklistedAccessToken.objects.filter(token=token).exists():
                return JsonResponse({
                    'detail': "This token has been revoked. Please login again."
                }, status=status.HTTP_401_UNAUTHORIZED)