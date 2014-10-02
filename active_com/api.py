from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


class SearchApiV2(object):

    def __init__(self, api_key):
        self.query_url = \
            'http://api.amp.active.com/v2/search?api_key=%s' % api_key

    def _append_query(self, **request):
        """
        Appends query

        :param request: HTTP GET request to append
        :return: self.query_url with appended HTTP GET keys and vals
        """

        url_parts = list(urlparse(self.query_url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(request)
        url_parts[4] = urlencode(query)

        query = urlunparse(url_parts)
        self.query_url = query.replace('%2C', ',')  # fix commas
        return self.query_url

    def near(self, near):
        """
        :param near: A string naming a place that can be geocoded.
        If the near string is not geocodable, returns a failed
        geocoded error.

        Example: San%20Diego,CA,US
        """
        self._append_query(near=near)
        return self.query_url

    def lat_lon(self, lat, lon):
        """
        A location specified as a latitude and longitude.
        :param lat: latitude, example: 43.2
        :param lon: latitude, example: -118
        """
        self._append_query(lat_lon="%s,%s" % (lat, lon))
        return self.query_url

    def bbox(self):
        """
        Not Implemented. I'm lazy.
        """
        raise NotImplementedError

    def geo_points(self):
        """
        Not Implemented. I'm lazy.
        """
        raise NotImplementedError

    def radius(self, miles=None, kilometers=None):
        """
        The search radius as specified in miles or kilometers

        :param miles: The search radius as specified in miles
        :param kilometers: The search radius as specified in kilometers
        """

        assert miles or kilometers
        assert not(miles and kilometers)

        miles = miles or kilometers * 0.621371

        self._append_query(radius=miles)
        return self.query_url

    def city(self, city):
        """
        Matches assets by city name.

        :param city: city name
        """
        self._append_query(city=city)
        return self.query_url

    def state(self, state):
        """
        Matches assets by state or province code

        :param state: state or province code
        """
        self._append_query(state=state)
        return self.query_url

    def zip(self, zip):
        """
        Matches assets by zip or postal code

        :param zip: zip or postal code
        """
        self._append_query(zip=zip)
        return self.query_url

    def country(self, country):
        """
        Matches assets by country name

        :param country: country name
        """
        self._append_query(country=country)
        return self.query_url

    def query(self, query):
        """
        Search by keywords. The free-form query to search.
        Equivalent to what a user types in the search box.

        :param query: keywords
        """
        self._append_query(query=query)
        return self.query_url
