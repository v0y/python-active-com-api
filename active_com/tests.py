from unittest import TestCase
from urllib.parse import urlparse

from active_com.api import SearchApiV2


class SearchApiV2Tests(TestCase):

    def setUp(self):
        self.search_api = SearchApiV2('abc')
        self.base_query = 'http://api.amp.active.com/v2/search?api_key=abc'

    def assertQueriesEqual(self, query1, query2):
        parsed_query1 = list(urlparse(query1))
        parsed_query2 = list(urlparse(query2))

        self.assertListEqual(
            sorted(parsed_query1[4].split('&')),
            sorted(parsed_query2[4].split('&')))

        # check uri without GET values
        self.assertListEqual(parsed_query1[:4], parsed_query2[:4])

        # check GET values
        self.assertListEqual(
            sorted(parsed_query1[4].split('&')),
            sorted(parsed_query2[4].split('&')))

    def test_append_query_returns_query(self):
        query = self.search_api._append_query(key='val', key2='val 2')
        expected_query = self.base_query + '&key=val&key2=val+2'

        self.assertQueriesEqual(query, expected_query)

    def test_near(self):
        query = self.search_api.near('dupa')
        expected_query = self.base_query + '&near=dupa'

        self.assertQueriesEqual(query, expected_query)

    def test_lan_lot(self):
        query = self.search_api.lat_lon(52.2464391, '21.0334827')
        expected_query = self.base_query + '&lat_lon=52.2464391,21.0334827'

        self.assertQueriesEqual(query, expected_query)

    def test_radius(self):
        query = self.search_api.radius(kilometers=123)
        expected_query = self.base_query + '&radius=76.428633'
        self.assertQueriesEqual(query, expected_query)

        query = self.search_api.radius(miles=123)
        expected_query = self.base_query + '&radius=123'
        self.assertQueriesEqual(query, expected_query)

    def test_city(self):
        query = self.search_api.city('dupa')
        expected_query = self.base_query + '&city=dupa'
        self.assertQueriesEqual(query, expected_query)

    def test_state(self):
        query = self.search_api.state('CA')
        expected_query = self.base_query + '&state=CA'
        self.assertQueriesEqual(query, expected_query)

    def test_zip(self):
        query = self.search_api.zip('12345')
        expected_query = self.base_query + '&zip=12345'
        self.assertQueriesEqual(query, expected_query)

    def test_country(self):
        query = self.search_api.country('12345')
        expected_query = self.base_query + '&country=12345'
        self.assertQueriesEqual(query, expected_query)

    def test_query_string(self):
        query = self.search_api.query('marathon')
        expected_query = self.base_query + '&query=marathon'
        self.assertQueriesEqual(query, expected_query)

    def test_current_page(self):
        query = self.search_api.current_page('3')
        expected_query = self.base_query + '&current_page=3'
        self.assertQueriesEqual(query, expected_query)
