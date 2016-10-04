Changelog for incuna-test-utils
============================

upcoming
--------

* Add additional deprecated method `get_field_by_name`

v6.5.0
------

* Add `get_all_field_names` to compensate for deprecation of `Model._meta` functions in Django 1.10

v6.4.1
------

* Refactor `URLTestMixin.assert_url_matches_view` to check `view.__module__` as well as `view.__name__` when checking equality.

v6.4.0
------

* Add `APIExampleMixin` and `BaseAPIExampleTestCase` for testing API examples.

v6.3.1
------

* Ensure `assert_url_matches_view` fails if `.as_view()` has been forgotten.

v6.3.0
------

* Add `utils.field_names` helper function for model tests.

v6.2.7
------
* Clean deploy to PyPI to avoid including a folder that no longer exists in the wheel.

v6.2.6
------
* Return a file from `uploadable_file()` with a short name to avoid form validation errors.

v6.2.5
------
* Bugfix: Fix MANIFEST.in to include missing files.

v6.2.4
------
* Bugfix: Fix a naming conflict between packages.

v6.2.3
------
* Bugfix: Add a missing `__init__.py`.

v6.2.1, 6.2.2
-------------
* Bugfix: Ensure the methods and factory fields in `factories.images` all output Django
  File objects.

v6.2.0
------
* Add `factories.images` module with usefuls for handling images in tests.
  * Provide a `simple_png()` method that creates a 1x1 black .png file in memory.
  * Provide two factory field classes that help provide data for FileFields and
    ImageFields.
  * Provide an `uploadable_file()` method that creates something you can upload to a
    form in tests.

v6.1.0
------
* Add `assert_presence` to `BaseIntegrationTestCase`.
* Add multiple-assert methods that accept a dictionary of assertions to make, and
  methods that combine accessing the view, rendering it, and asserting the result.
* Add `make install` command to perform local installation of requirements.

v6.0.0
------
* Remove non-standard name attribute on `BaseUserFactory`
* Add `BaseAdminUserFactory`

v5.3.0
------
* Allow login username to use `USERNAME_FIELD`

v5.2.0
------
* Add `BaseAdminIntegrationTestCase`

v5.1.0
------
* Add `view_instance` method to RequestTestCase

v5.0.0
------
* Rename Python2CountEqualMixin to Python2AssertMixin
* Add assertRegex to Python2AssertMixin

v4.0.0
------
* Remove requirement for wrapping function-based views in staticmethod.
* Update factories to use `class Meta` with a `model` attribute instead of `FACTORY_FOR`
* Add tests for all code
* Fix various bugs caught by the new tests

v3.2.0
------
* Add ability to handle function-based views to BaseRequestTestCase.
* Add ability to augment requests with sessions to BaseRequestTestCase.
* Use both in IntegrationTestCase.
* Reflow IntegrationTestCase's methods for clarity and flexibility.
* Fix various bugs along the way.

v3.1.2
------
* Fix `super` call in `BaseAPIRequestTestCase`

v3.1.1
------
* Fix bug with DummyStorage object not being iterable when calling render().

v3.1.0
------
* Add `IntegrationTestCase` for testing rendered HTML pages.
* Replace `APIRequestTestCase` with `BaseRequestTestCase`.  Technically
  backwards-incompatible, but is essentially a bugfix from v3.0.0.

v3.0.0
------
* Replace `UserFactory` with `BaseUserFactory`.
* Remove `FACTORY_FOR` from `BaseUserFactory`.
* Replace `RequestTestCase` with `BaseRequestTestCase`.
* `BaseRequestTestCase` requires an explicit `user_factory` to be set when
  subclassing.

v2.1.0
------
* Add ability to override urlconf when using `assert_url_matches_view`.

v2.0.1
------
* Add `compat.DJANGO_LT_15` and `compat.DJANGO_LT_16`.

v2.0.0
------

* Add `compat` module.
* Add `compat.DJANGO_LT_17`.
* Add `compat.wipe_id_fields_on_django_lt_17`.
* Move the Python2CountEqualMixin from `testcases.compat` to `compat`.

v1.1.1
------

* Fix URLTestCase
    * Check for cls attribute on `resolved_view`, not view

v1.1.0
------
* Remove AbstractModelMixin
    * AbstractModelMixin creates multiple versions of the same model class. This
      confuses the django 1.7 App loader.
    * Use a concrete subclass of your abstract model in your test directory
      instead.

v1.0.0
------
* Simplify testcases.urls
    * Add URLTestMixin with `assert_url_matches_view` method
    * Remove URLsTestCaseREST, URLsTestCaseViewMethod and URLsTestCase
    * Remove URLsMixinREST, URLsMixinForViewMethod, URLsMixin and URLsMixinBase

v0.7.0
------
* Add Python2CountEqualMixin to enable use of assertCountEqual in python 2

v0.6
------
* Add URLsTestCaseREST and URLsTestCaseViewMethod for cleanliness and ease of use
* Deprecate URLsTestCase

v0.5
------
* Refine URLsMixin into two classes, URLsMixinForViewMethod and URLsMixinREST
* Deprecate URLsMixin

v0.4
------
* Add URLsMixin and URLsTestCase
* Support wheel

v0.3
------
* Add RequestTestCase.


v0.2.1
------
* Remove app-specific tearDown logic from AbstractModelMixin


v0.2.0
------
* Add PageFactory for FeinCMS

v0.1.2
------
* Convert AbstractModelTestCase to mixin.


v0.1.1
------
* Refactor testcases

v0.1
------
Initial release.

Add:

* APITestCase
* AbstractModelTestCase
* UserFactory

