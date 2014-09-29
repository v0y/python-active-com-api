from unittest import TestCase
from urllib.parse import urlparse

from active_com.api import SearchApiV2


class SearchApiV2Tests(TestCase):

    def setUp(self):
        self.search_api = SearchApiV2('abc')

    def test_append_query_returns_query(self):
        query = self.search_api._append_query(key='val', key2='val 2')
        expected_query = \
            'http://api.amp.active.com/v2/search?' \
            'key=val&key2=val+2&api_key=abc'

        parsed_query = list(urlparse(query))
        parsed_expected_query = list(urlparse(expected_query))

        # check uri without GET values
        self.assertListEqual(parsed_query[:4], parsed_expected_query[:4])

        # check GET values
        self.assertListEqual(
            sorted(parsed_query[4].split('&')),
            sorted(parsed_expected_query[4].split('&')))
