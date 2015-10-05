from unittest import TestCase

from incuna_test_utils.testcases.api_examples import APIExampleMixin


class TestAPIExampleMixin(APIExampleMixin, TestCase):
    EXAMPLES_DIR = 'tests/testcases/examples'

    def test_api_example_json_file(self):
        file_path = self.api_example_json_file('/users/pk', 'get')

        expected_path = self.EXAMPLES_DIR + '/users/pk/get.json'
        assert file_path == expected_path

    def test_api_example_data(self):
        data = self.api_example_data('/users/pk', 'get')

        expected_data = {
            'description': 'Information about a user',
            'url': '/users/<pk>',
            'OK': {
                'status': 200,
                'response_data':  {
                    'url': 'http://localhost:8000/users/1',
                    'name': 'Arthur, King of the Britons',
                    'quest': 'To seek the holy Grail',
                },
            },
        }
        assert data == expected_data


class TestAdjustForPKs(APIExampleMixin, TestCase):
    """
    adjust_for_pks() is quite finicky, so verifying independently that it works seems
    like a good idea.
    """

    api_data = {
        'url_one': 'http://localhost:8000/endpoint/1',
        'url_two': 'http://localhost:8000/endpoint/2',
        'url_twenty': 'http://localhost:8000/endpoint/20',
        'pk_one': 1,
        'pk_two': 2,
        'unaffected_field': 'unaffected',
        'unaffected_boolean': True,  # To test that it doesn't get confused for 1
    }

    def expected_data(self, **changes):
        expected = {}  # Don't modify self.api_data in place.
        expected.update(self.api_data)

        expected.update(changes)
        return expected

    def test_noop(self):
        """When nothing is meant to change, sanity-check that nothing actually changes."""
        adjusted = self.adjust_for_pks(self.api_data, object_pk=1, pk_to_replace=1)

        assert adjusted == self.api_data

    def test_replace_simple(self):
        """An ordinary replace operation, swapping pk=1 for pk=4."""
        adjusted = self.adjust_for_pks(self.api_data, object_pk=4, pk_to_replace=1)

        expected = self.expected_data(
            url_one='http://localhost:8000/endpoint/4',
            pk_one=4,
        )
        assert adjusted == expected
        # And it doesn't affect the original data.
        assert adjusted != self.api_data

    def test_replace_awkward(self):
        """
        Trying to replace pk=2 catches pk=20 in the URLs at the moment as well.

        Would be nice if it didn't - there's some option for using regular expressions
        and a more complicated structure to replace the three specific cases of /pk$,
        /pk/, and /pk?getarg=blah.  Possibly more, too.  At the moment the method is
        dumb enough to make the mistake, but it's an edge case.  In situations where
        you're likely to have two different PKs in your API by Example spec, you can
        number them in the spec so as not to clash (which is clearer) and/or use
        field_names to replace only on specific entries.

        Essentially, fixing this edge case is awkward enough that it's not massively
        worth it, but this test documents the strangeness (and will tell you if it
        gets fixed).
        """
        adjusted = self.adjust_for_pks(self.api_data, object_pk=4, pk_to_replace=2)

        expected = self.expected_data(
            url_two='http://localhost:8000/endpoint/4',
            pk_two=4,
            url_twenty='http://localhost:8000/endpoint/40',  # sadness
        )
        assert adjusted == expected

    def test_field_names(self):
        """Test that setting field_names replaces only in the named fields."""
        field_names = ['url_one', 'unaffected_field']
        adjusted = self.adjust_for_pks(
            self.api_data,
            object_pk=4,
            pk_to_replace=1,
            field_names=field_names
        )

        # This is the same operation as test_replace_simple, but only url_one is changed
        expected = self.expected_data(url_one='http://localhost:8000/endpoint/4')
        assert adjusted == expected
