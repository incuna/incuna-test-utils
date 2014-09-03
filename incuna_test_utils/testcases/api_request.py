from rest_framework.test import APIRequestFactory, force_authenticate

from .request import BaseRequestTestCase


class BaseAPIRequestTestCase(BaseRequestTestCase):
    """
    Extend BaseRequestTestCase with REST framework compatibility.

    Must be subclassed with an user_factory attribute in order to work.
    """
    request_factory = APIRequestFactory

    def create_request(self, method='get', url='/', user=None, auth=True, **kwargs):
        kwargs['format'] = 'json'
        request = super(BaseAPIRequestTestCase, self).create_request(
            method=method,
            url=url,
            user=user,
            auth=auth,
            **kwargs)
        if auth:
            force_authenticate(request, request.user)
        return request
