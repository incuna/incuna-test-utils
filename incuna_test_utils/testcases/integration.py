from django.shortcuts import render

from .request import BaseRequestTestCase


class DummyStorage:
    def __init__(self):
        self.store = set()

    def add(self, level, message, extra_tags=''):
        self.store.add(message)


class BaseIntegrationTestCase(BaseRequestTestCase):
    """
    A TestCase that operates similarly to a Selenium test.

    Contains methods that access pages and render them to strings full of
    HTML.  Can be used to assert the contents of templates as well as doing
    normal TestCase things.

    Must be subclassed with a user_factory attribute in order to work.
    """
    def access_view(self, request, **kwargs):
        """Helper method that accesses the view."""
        view = self.view_class.as_view()
        response = view(request, **kwargs)
        return response

    def render_to_str(self, request, response):
        """Render a HTTPResponse into a string that holds the HTML content."""
        response = render(request, response.template_name, response.context_data)
        return str(response.content)

    def access_assert_and_render(self, as_user, expected_status=200, **kwargs):
        """
        Accesses the view as the named user and returns a string of HTML.

        Combines access_view, an assertion on the returned status, and
        render_to_str.  Also creates a request for you.
        """
        request = self.create_request(user=as_user)
        request._messages = DummyStorage()
        response = self.access_view(request, **kwargs)
        self.assertEqual(expected_status, response.status_code)
        return self.render_to_str(request, response)

    def assert_count(self, needle, haystack, count=1):
        """
        Assert that 'needle' occurs exactly 'count' times in 'haystack'.

        Used as a snazzier, stricter version of unittest.assertIn.
        The 'count' parameter defaults to 1.

        Outputs a decently verbose error message when it fails.
        """
        actual_count = haystack.count(needle)
        self.assertEqual(
            count,
            actual_count,
            'Expected {count} instance{plural} of {needle}, but found {actual_count}, in {haystack}'.format(
                count=count,
                plural=('' if count==1 else 's'),
                needle=needle,
                actual_count=actual_count,
                haystack=haystack,
            )
        )