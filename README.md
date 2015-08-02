# incuna-test-utils
[![Build Status](https://travis-ci.org/incuna/incuna-test-utils.svg?branch=master)](https://travis-ci.org/incuna/incuna-test-utils?branch=master)


Incuna Test Utils is a collection of TestCases and other helpers for testing
Django apps.


## TestCases


These are found in `incuna_test_utils.testcases`.


### `urls.URLTestCase`


`URLTestCase` adds `assert_url_matches_view` to check a url has been configured
to use the correct view.


### `request.BaseRequestTestCase`


`BaseRequestTestCase` provides various helper methods for working with django
views:

  * `get_view` returns a view callable based on a `view` attribute set on the
`TestCase` class. `view` can be either a function-based or a class-based view.
  * `view_instance` returns an instance of a class-based `view` attribute set
on the `TestCase` class. `view_instance` accepts a `request` and `*args` and
`**kwargs`. These are set on the `view` instance.
  * `add_session_to_request` gives a `request` a `session`.
  * `create_user` returns a `user` using either `AnonymousUser` or a
`user_factory` attribute set on the `TestCase`. The `user_factory` should have
a `create` method that returns a `user`.
[`factory_boy`](http://factoryboy.readthedocs.org/en/latest/index.html) is recommended.
  * `create_request` wraps Django's `RequestFactory` to provide useful defaults.
It returns a `request` with `user` and `_messages` attributes. It can also set
`DATA` and `session` on the `request`.


### `integration.BaseAdminIntegrationTestCase`


`BaseAdminIntegrationTestCase` provides a `TestCase` to test the django admin actions
such as `add`, `change`, `changelist` and `delete`.
`BaseAdminIntegrationTestCase` should be subclassed and should define two attributes:
 - a `user_factory` to create an authenticated client;
 - a `model` to test.

Example:
```python
from incuna_test_utils.testcases.integration import BaseAdminIntegrationTestCase


class TestUserAdmin(BaseAdminIntegrationTestCase):
    user_factory = factories.UserFactory
    model = ModelToTest

    def test_admin_add_page(self):
        response = self.get_admin_add_page()
        self.assertEqual(response.status_code, 200)

    ...
```


### `integration.BaseIntegrationTestCase`


`BaseIntegrationTestCase` extends `BaseRequestTestCase` and adds more helper
methods useful for integration tests:

  * `access_view` creates a `request`, calls the `TestCase`'s `view` and returns
a `response`.
  * `render_to_str` renders a `response` using a `request`, `response.template_name`
and `response.context_data`. If a `request` is not provided, `render_to_str` uses
`response.request`.
  * `access_view_and_render_response` wraps `access_view` and `render_to_str`.
It also checks the `response.status_code` is as expected. The default
`expected_status` is `200` (`HTTP_OK`).
  * `assert_presence` checks that an item does or doesn't appear in a container.
  * `assert_count` checks that an item appears in a container an expected number
of times.
  * `assert_presence_multiple` and `assert_count_multiple` run one or more assertions in
  a single method call.
  * `render_view_and_assert_content` and `render_view_and_assert_content_counts` combine
  a call to `access_view_and_render_response` with a multiple-assert call on the result.


### `api_request.BaseAPIRequestTestCase`


`BaseAPIRequestTestCase` extends `BaseRequestTestCase` for use with
[`django-rest-framework`](http://www.django-rest-framework.org/).

* `create_request` is overriden to use rest framework's
[`APIRequestFactory`](http://www.django-rest-framework.org/api-guide/testing#apirequestfactory).
It also sets `request.format` to `'json'`. If called with `auth=True` (the default),
`create_request` also calls
[`force_authenticate`](http://www.django-rest-framework.org/api-guide/testing#forcing-authentication).


## Factories


These are found in `incuna_test_utils.factories`. They require
[`factory_boy`](http://factoryboy.readthedocs.org/en/latest/index.html).


### `user.BaseUserFactory`


This defines a simple factory with an `email` attribute. This can be used with
a custom User model that has these fields:

```python
    class UserFactory(BaseUserFactory):
        class Meta:
            model = User
```


### `user.BaseAdminUserFactory`


`BaseAdminUserFactory` defines a user with `is_active`, `is_staff` and
`is_superuser` to `True`. This factory also defines a post hook which
sets a default password accessible with `raw_password`.


### `feincms_page.PageFactory`


This factory can be used to create instances of
[`Feincms`](http://feincms-django-cms.readthedocs.org/en/latest/index.html)'s
[`Page`](http://feincms-django-cms.readthedocs.org/en/latest/page.html) model.


## `compat`


`compat` provides a few miscelleaneous helpers useful for testing cross-version
code:

  * `DJANGO_LT_15`, `DJANGO_LT_16`, `DJANGO_LT_17` each return `True` if
`django.VERSION` is less than `1.5`, `1.6` or `1.7` respectively.
  * `wipe_id_fieldson_django_lt_17` removes any field name ending in `_id` from
a collection if the django version is less than `1.7`. This is useful for testing
a model has the fields expected.
  * `Python2AssertMixin` aliases python 2.7 assert methods to match the python 3 api.
    * `TestCase.assertItemsEqual` is aliased as `assertCountEqual`
    * `TestCase.assertRegexpMatches` is aliased as `assertRegex`
