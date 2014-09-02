Changelog for incuna-test-utils
============================

Upcoming v3.1.0
------
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
    * Check for cls attribute on resolved_view, not view

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
    * Add URLTestMixin with assert_url_matches_view method
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

