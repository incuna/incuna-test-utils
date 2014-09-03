from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render

from .request import BaseRequestTestCase


class BaseIntegrationTestCase(BaseRequestTestCase):
    """
    A TestCase that operates similarly to a Selenium test.

    Contains methods that access pages and render them to strings full of
    HTML.  Can be used to assert the contents of templates as well as doing
    normal TestCase things.

    Must be subclassed with the following attributes in order to work:
    * user_factory
    * view_class (class-based view) or view (method-based view)
    """
    def get_view(self):
        """
        Returns the class's attached view.

        Checks self.view_class, then self.view.  Throws an ImproperlyConfigured
        exception if neither exist.
        """
        try:
            return self.view_class.as_view()
        except AttributeError:
            # Continue on to the next try/catch
            pass
        
        try:
            return self.view
        except AttributeError:
            message = "This test must have a 'view_class' or 'view' attribute."
            raise ImproperlyConfigured(message)

    def access_view(self, *args, request=None, **kwargs):
        """
        Helper method that accesses the test's view.

        Accepts a request parameter, which can be None.  If it is, this method
        creates a basic request on your behalf.

        Returns a HTTPResponse object with the request (created or otherwise)
        attached.
        """
        if request is None:
            request = self.create_request()
            request._messages = DummyStorage()

        view = self.get_view()
        response = view(request, *args, **kwargs)

        # Add the request to the response.
        # This is a weird-looking but compact way of ensuring we have access to
        # the request everywhere we need it, without doing clunky things like
        # returning tuples all the time.
        response.request = request
        return response

    def render_to_str(self, response, request=None):
        """
        Render a HTTPResponse into a string that holds the HTML content.
        """
        if response.request:
            # Use the response's attached request if we have it.
            request = response.request

        response = render(request, response.template_name, response.context_data)
        return str(response.content)

    def access_view_and_render_response(self, *view_args, request=None, expected_status=200, **view_kwargs):
        """
        Accesses the view and returns a string of HTML.

        Combines access_view, an assertion on the returned status, and
        render_to_str.

        Accepts an optional request (but will create a simple one if the
        parameter isn't supplied), an expected status code for the response
        (which defaults to 200), and args and kwargs for the view method.
        """
        response = self.access_view(*view_args, request=request, **view_kwargs)
        self.assertEqual(expected_status, response.status_code)
        return self.render_to_str(response)

    def assert_count(self, needle, haystack, count):
        """
        Assert that 'needle' occurs exactly 'count' times in 'haystack'.

        Used as a snazzier, stricter version of unittest.assertIn.
        Outputs a verbose error message when it fails.
        """
        actual_count = haystack.count(needle)

        # Build a verbose error message in case we need it.
        plural = '' if count == 1 else 's'
        message = 'Expected {count} instance{plural} of {needle}, but found {actual_count}, in {haystack}'
        message = message.format_map(locals())

        # Make the assertion.
        self.assertEqual(count, actual_count, message)
