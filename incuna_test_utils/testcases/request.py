from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory


class DummyStorage:
    def __init__(self):
        self.store = list()

    def add(self, level, message, extra_tags=''):
        self.store.add(message)

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
    view, abstracting over whether it's class- or function-based.  However,
    due to a quirk of Python's way of attaching things to classes, any
    function-based view must currently be added wrapped in `staticmethod()`:
        view = view_class                   # class-based view
        view = staticmethod(view_func)      # function-based view
    """
    request_factory = RequestFactory 

    def get_view(self):
        """
        Returns the class's attached view, as a callable.

        Checks self.view exists, and throws an ImproperlyConfigured exception
        if it doesn't.  Otherwise, it returns the view, ensuring it's callable.
        """
        try:
            view = self.view
        except AttributeError:
            message = "This test must have a 'view' attribute."
            raise ImproperlyConfigured(message)
        
        try:
            return view.as_view()
        except AttributeError:
            return view

    @staticmethod
    def add_session_to_request(request):
        """Annotate a request object with a session."""
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

    def create_request(self, method='get', url='/', user=None, auth=True, add_session=False, **kwargs):
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
