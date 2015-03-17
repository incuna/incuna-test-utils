# -*- coding: utf-8 -*-
import pytest
from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from incuna_test_utils.testcases.integration import BaseIntegrationTestCase
from tests.factories import UserFactory
from tests.views import my_view, MyTemplateView


TEMPLATE_CONTENT = u'†εмρʟαтℯ ℭøηт℮ηт.\n'


@pytest.fixture(scope='module')
def simple_integration():
    class IntegrationTestCase(BaseIntegrationTestCase):
        user_factory = UserFactory
        view = my_view

    # Python 2 doesn't allow instantiation of a TestCase without a
    # specified test method, so specify a method known to exist on
    # all TestCase instances. We don't care which method this is.
    return IntegrationTestCase(methodName='__init__')


@pytest.fixture(scope='module')
def template_view_integration():
    class IntegrationTestCase(BaseIntegrationTestCase):
        user_factory = UserFactory
        view = MyTemplateView

    # Python 2 doesn't allow instantiation of a TestCase without a
    # specified test method, so specify a method known to exist on
    # all TestCase instances. We don't care which method this is.
    return IntegrationTestCase(methodName='__init__')


class TestIntegration:
    @pytest.mark.django_db
    def test_access_view(self, simple_integration):
        response = simple_integration.access_view()
        assert isinstance(response, HttpResponse)

        request = response.request
        assert isinstance(request, WSGIRequest)
        assert isinstance(request.session, SessionBase)

    @pytest.mark.django_db
    def test_access_view_request(self, simple_integration):
        request = simple_integration.create_request()
        response = simple_integration.access_view(request=request)

        assert response.request == request

        with pytest.raises(AttributeError):
            response.request.session

    def test_render_to_str(self, template_view_integration):
        request = template_view_integration.create_request(auth=False)
        response = template_view_integration.access_view(request=request)

        content = template_view_integration.render_to_str(response)
        assert content == TEMPLATE_CONTENT

    def test_access_view_and_render_response(self, template_view_integration):
        request = template_view_integration.create_request(auth=False)

        content = template_view_integration.access_view_and_render_response(
            request=request,
        )
        assert content == TEMPLATE_CONTENT

    def test_assert_count(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        count = 4
        simple_integration.assert_count(needle, haystack, count)

    def test_assert_count_fail(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        count = 19

        with pytest.raises(AssertionError):
            simple_integration.assert_count(needle, haystack, count)

    def test_assert_presence(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        is_present = True
        simple_integration.assert_presence(needle, haystack, is_present)

    def test_assert_presence_fail(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        is_present = False

        with pytest.raises(AssertionError):
            simple_integration.assert_presence(needle, haystack, is_present)

    def test__assert_count_message(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        count = 1
        actual_count = haystack.count(needle)

        expected_message_args = (count, needle, actual_count, haystack)
        expected_message = 'Expected {} instance of {}, but found {}, in {}'
        expected_message = expected_message.format(*expected_message_args)

        message_args = (needle, haystack, count, actual_count)
        message = simple_integration._assert_count_message(*message_args)
        assert message == expected_message

    def test__assert_count_message_plural(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        count = 7
        actual_count = haystack.count(needle)

        expected_message_args = (count, needle, actual_count, haystack)
        expected_message = 'Expected {} instances of {}, but found {}, in {}'
        expected_message = expected_message.format(*expected_message_args)

        message_args = (needle, haystack, count, actual_count)
        message = simple_integration._assert_count_message(*message_args)
        assert message == expected_message

    def test__assert_presence_message(self, simple_integration):
        haystack = 'aabacad'
        needle = 'a'
        presence = False

        expected_message = 'Expected not to find {} in {}'
        expected_message = expected_message.format(needle, haystack)

        message_args = (needle, haystack, presence)
        message = simple_integration._assert_presence_message(*message_args)
        assert message == expected_message

    def test__assert_presence_message_present(self, simple_integration):
        haystack = 'aabacad'
        needle = '18'
        presence = True

        expected_message = 'Expected to find {} in {}'
        expected_message = expected_message.format(needle, haystack)

        message_args = (needle, haystack, presence)
        message = simple_integration._assert_presence_message(*message_args)
        assert message == expected_message

    def test_assert_count_multiple(self, simple_integration):
        haystack = 'aabacad'
        assertions = {
            'a': 4,
            'b': 1,
        }

        simple_integration.assert_count_multiple(haystack, **assertions)

    def test_assert_count_multiple_fail(self, simple_integration):
        haystack = 'aabacad'
        assertions = {
            'a': 4,
            'b': 7,
        }

        with pytest.raises(AssertionError):
            simple_integration.assert_count_multiple(haystack, **assertions)

    def test_assert_presence_multiple(self, simple_integration):
        haystack = 'aabacad'
        assertions = {
            'a': True,
            'z': False,
        }

        simple_integration.assert_presence_multiple(haystack, **assertions)

    def test_assert_presence_multiple_fail(self, simple_integration):
        haystack = 'aabacad'
        assertions = {
            'a': True,
            'z': True,
        }

        with pytest.raises(AssertionError):
            simple_integration.assert_presence_multiple(haystack, **assertions)

    @pytest.mark.django_db
    def test_render_view_and_assert_content(self, template_view_integration):
        assertions = {
            TEMPLATE_CONTENT: True,
        }

        template_view_integration.render_view_and_assert_content(assertions)

    @pytest.mark.django_db
    def test_render_view_and_assert_content_fail(self, template_view_integration):
        assertions = {
            'A string not in the template content': True,
        }

        with pytest.raises(AssertionError):
            template_view_integration.render_view_and_assert_content(assertions)

    @pytest.mark.django_db
    def test_render_view_and_assert_content_counts(self, template_view_integration):
        assertions = {
            TEMPLATE_CONTENT: 1,
        }

        template_view_integration.render_view_and_assert_content_counts(assertions)

    @pytest.mark.django_db
    def test_render_view_and_assert_content_counts_fail(self, template_view_integration):
        assertions = {
            TEMPLATE_CONTENT: 6,
        }

        with pytest.raises(AssertionError):
            template_view_integration.render_view_and_assert_content_counts(assertions)
