from rest_framework.test import APIRequestFactory, force_authenticate

from .request import RequestTestCase


class APIRequestTestCase(RequestTestCase):
    request_factory = APIRequestFactory

    def create_request(self, method='get', url='/', user=None, auth=True, **kwargs):
        kwargs['format'] = 'json'
        request = super(APIRequestTestCase, self).create_request(
            method=method,
            url=url,
            user=user,
            auth=auth,
            **kwargs)
        if auth:
            force_authenticate(request, request.user)
        return request
