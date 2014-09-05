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
    * view (class-based or function-based view)
    """

    def access_view(self, *args, **kwargs):
        """
        Helper method that accesses the test's view.

        Accepts an optional 'request' kwarg.  If this isn't supplied,
        access_view creates a basic request on your behalf.

        Returns a HTTPResponse object with the request (created or otherwise)
        attached.
        """
        request = kwargs.pop('request', None)
        if request is None:
            request = self.create_request(add_session=True)

        view_callable = self.get_view()
        response = view_callable(request, *args, **kwargs)

        # Add the request to the response.
        # This is a weird-looking but compact way of ensuring we have access to
        # the request everywhere we need it, without doing clunky things like
        # returning tuples all the time.
        response.request = request
        return response

    def render_to_str(self, response, request=None):
        """
        Render a HTTPResponse into a string that holds the HTML content.

        Accepts an optional request parameter, and looks for a request attached
        to the response if the optional parameter isn't specified.
        """
        if request is None:
            request = response.request

        response = render(request, response.template_name, response.context_data)
        return response.content.decode('utf-8')

    def access_view_and_render_response(self, *args, **kwargs):
        """
        Accesses the view and returns a string of HTML.

        Combines access_view, an assertion on the returned status, and
        render_to_str.

        Accepts an optional 'request' kwarg holding a HTTPRequest, but will
        create a simple one if the parameter isn't supplied, and
        'expected_status', an expected status code for the response, which
        defaults to 200.  Other args and kwargs are passed on to the view
        method.
        """
        request = kwargs.pop('request', None)
        expected_status = kwargs.pop('expected_status', 200)

        response = self.access_view(*args, request=request, **kwargs)

        # Assert that the response has the correct status code before we go
        # any further.  Throwing accurately descriptive failures when something
        # goes wrong is better than trying to run assertions on the content
        # of a HTML response for some random 404 page.
        self.assertEqual(expected_status, response.status_code)

        # Render the response and return it.
        return self.render_to_str(response)

    @staticmethod
    def _assert_count_message(needle, haystack, count, actual_count):
        # Build a verbose error message in case we need it.
        plural = '' if count == 1 else 's'
        message = 'Expected {count} instance{plural} of {needle}, but found {actual_count}, in {haystack}'
        return message.format(
            count=count,
            plural=plural,
            needle=needle,
            actual_count=actual_count,
            haystack=haystack,
        )

    def assert_count(self, needle, haystack, count):
        """
        Assert that 'needle' occurs exactly 'count' times in 'haystack'.

        Used as a snazzier, stricter version of unittest.assertIn.
        Outputs a verbose error message when it fails.
        """
        actual_count = haystack.count(needle)

        message_args = (needle, haystack, count, actual_count)
        message = self._assert_count_message(*message_args)

        self.assertEqual(count, actual_count, message)
