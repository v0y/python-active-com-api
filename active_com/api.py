from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


class SearchApiV2(object):

    def __init__(self, api_key):
        self.query = 'http://api.amp.active.com/v2/search?api_key=%s' % api_key

    def _append_query(self, **request):
        """
        Appends query

        :param request: HTTP GET request to append
        :return: self.query with appended HTTP GET keys and vals
        """

        url_parts = list(urlparse(self.query))
        query = dict(parse_qsl(url_parts[4]))
        query.update(request)
        url_parts[4] = urlencode(query)

        self.query = urlunparse(url_parts)
        return self.query

    def near(self, near):
        """
        :param near: A string naming a place that can be geocoded.
        If the near string is not geocodable, returns a failed
        geocoded error.

        Example: San%20Diego,CA,US
        """
        self._append_query(near=near)
        return self.query
