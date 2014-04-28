import warnings

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase


class URLsMixinBase(object):
    """A TestCase Mixin with a check_url helper method for testing urls"""

    def check_url(self, view, expected_url, url_name,
                  url_args=None, url_kwargs=None):
        """
        Assert a view's url is correctly configured

        Check the url_name reverses to give a correctly formated expected_url.
        Check the expected_url resolves to the correct view.
        """

        reversed_url = reverse(url_name, args=url_args, kwargs=url_kwargs)
        self.assertEqual(reversed_url, expected_url)

        self.assertViewNames(view, expected_url)

    def assertViewNames(self, view, expected_url):
        """
        Assert that the view method/class that the URL resolves to is the
        correct one.
        """
        raise NotImplementedError


class URLsMixinForViewMethod(URLsMixinBase):
    """For testing method-based views."""

    def assertViewNames(self, view_method, expected_url):
        resolved_view_method = resolve(expected_url).func
        self.assertEqual(resolved_view_method.__name__, view_method.__name__)


class URLsMixinREST(URLsMixinBase):
    """For testing class-based views."""

    def assertViewNames(self, view_class, expected_url):
        resolved_view_class = resolve(expected_url).func.cls
        self.assertEqual(resolved_view_class, view_class)


class URLsMixin(URLsMixinREST):
    """For backwards compatibility."""
    warnings.warn(
        'URLsMixin is deprecated; use URLsMixinREST instead.',
        DeprecationWarning)


class URLsTestCase(URLsMixinREST, TestCase):
    pass
