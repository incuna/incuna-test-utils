from django.core.urlresolvers import resolve, reverse
from django.test import TestCase


class URLsTestCase(TestCase):
    """A TestCase with a check_url helper method for testing urls"""

    def check_url(self, view_class, url, url_name, url_args=None, url_kwargs=None):
        """
        Assert a view's url is correctly configured

        Check the url_name reverses to give a correctly formated url.
        Check the url resolves to the correct view.
        """

        reversed_url = reverse(url_name, args=url_args, kwargs=url_kwargs)
        self.assertEqual(reversed_url, url)

        resolved_view_class = resolve(url).func.cls
        self.assertEqual(resolved_view_class, view_class)
