Changelog for incuna-test-utils
============================

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

