from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


class SearchApiV2(object):

    def __init__(self, api_key):
        self.query = 'http://api.amp.active.com/v2/search?api_key=%s' % api_key

    def _append_query(self, **request_dict):
        """
        Appends query

        :param request_dict: dict of HTTP GET request to append
        :return: self.query with appended HTTP GET keys and vals
        """

        url_parts = list(urlparse(self.query))
        query = dict(parse_qsl(url_parts[4]))
        query.update(request_dict)
        url_parts[4] = urlencode(query)

        return urlunparse(url_parts)
