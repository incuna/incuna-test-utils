from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.exceptions import ImproperlyConfigured
from django.test import RequestFactory, TestCase


class DummyStorage:
    def __init__(self):
        self.store = list()

    def add(self, level, message, extra_tags=''):
        self.store.append(message)

    def __iter__(self):
        for item in self.store:
            yield item


class BaseRequestTestCase(TestCase):
    """
    Extend django.test.TestCase with a create_request method.

    BaseRequestTestCase must be subclassed with a user_factory attribute to
    create a default user for the request.

    A class- or function-based view can be attached to the test class as the
    'view' attribute.  get_view() returns a callable version of that
    view, abstracting over whether it's class- or function-based.
    """

    request_factory = RequestFactory

    @classmethod
    def get_view(cls):
        """
        Returns the class's attached view, as a callable.

        Checks self.view exists, and throws an ImproperlyConfigured exception
        if it doesn't.  Otherwise, it returns the view, ensuring it's callable.
        """
        try:
            view = cls.__dict__['view']
        except KeyError:
            message = "This test must have a 'view' attribute."
            raise ImproperlyConfigured(message)

        try:
            return view.as_view()
        except AttributeError:
            return view

    @classmethod
    def view_instance(cls, request=None, *args, **kwargs):
        """
        Returns an instance of the class's attached view.

        Checks self.view exists, and throws an ImproperlyConfigured exception
        if it doesn't.  Otherwise, it returns the view instance with request,
        args and kwargs set.
        """
        try:
            view = cls.view
        except AttributeError:
            message = "This test must have a 'view' attribute."
            raise ImproperlyConfigured(message)

        return view(request=request, args=args, kwargs=kwargs)

    @staticmethod
    def add_session_to_request(request):
        """Annotate a request object with a session."""
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

    def create_request(
        self,
        method='get',
        url='/',
        user=None,
        auth=True,
        add_session=False,
        **kwargs
    ):
        if user is None:
            user = self.create_user(auth=auth)
        request = getattr(self.request_factory(), method)(url, **kwargs)
        request.user = user

        if 'data' in kwargs:
            request.DATA = kwargs['data']

        request._messages = DummyStorage()

        if add_session:
            self.add_session_to_request(request)

        return request

    def create_user(self, auth=True, **kwargs):
        if auth:
            return self.user_factory.create(**kwargs)
        else:
            return AnonymousUser()
