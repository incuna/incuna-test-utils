import json


class APIExampleMixin:
    """A TestCase mixin that allows access to API by Example retrieval methods."""

    def api_example_json_file(self, url, method):
        """
        Return the API example at a location generated from the view URL and method.

        All URL kwargs in the URL are given only by their names, no other characters.
        For example:
            for POSTing to a view at `/patients/<pk>`,
            call self.api_example_json_file('/patients/pk', 'post')
            and you'll get 'api-description/patients/pk/post.json'
        """
        return '{base}{url}/{method}.json'.format(
            base=self.EXAMPLES_DIR,
            url=url,
            method=method,
        )

    def api_example_data(self, url, method):
        """Return the API example for this view URL and method, as a dictionary."""
        file_path = self.api_example_json_file(url, method)
        with open(file_path) as data_file:
            return json.load(data_file)

    def adjust_for_pks(self, data, object_pk, pk_to_replace=1, field_names=None):
        """
        Replace <pk_to_replace> with <object_pk> in the given data.

        Generally, the API description will be written with specific, 'hard-coded' pks.
        There's no other real way to do it, but it's a bit fiddly in tests when you
        don't know what the pk of, say, an object created by a POST will be.

        This method fixes that by modifying URL and pk fields in order to match them up
        to the specified <object_pk>.

        The method as written is very dumb.  Rather than trying to guess what a pk or
        a URL field looks like, it just looks for occurrences of '/<pk>' in strings and
        numbers that equal <pk>.  It can be limited to a set of specific fields to
        operate on, if you need to deal with special cases.

        The method copies the data dictionary in order to operate non-destructively,
        since you might need to run it several times with different `field_names` values.
        """
        url_pk_to_replace = '/{}'.format(pk_to_replace)
        url_object_pk = '/{}'.format(object_pk)

        # Copy data rather than modifying it in-place.
        adjusted_data = {}
        adjusted_data.update(data)

        if not field_names:
            field_names = adjusted_data.keys()

        for key in field_names:
            value = adjusted_data[key]
            if isinstance(value, str):
                adjusted_data[key] = value.replace(url_pk_to_replace, url_object_pk)
            elif value == pk_to_replace and not isinstance(value, bool):
                adjusted_data[key] = object_pk

        return adjusted_data
