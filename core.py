import bitly_api
import pyshorteners

# TODO: Get the url to the shortner
# TODO: Create a hash of the url
# TODO: Create a short url
# TODO: Return the short url


class TinyUrlShortner(object):
    """URL SHORTNER USING TINYURL

    Args:
        object ([type]): Url shortner extends from object
    """

    def __init__(self, url: str):
        self.url: str = url
        self.shortner = pyshorteners.Shortener()

    def get_url(self):
        return self.url

    def short_url(self):
        return self.shortner.tinyurl.short(self.url)


class BitlyUrlShortner(object):
    """Bitly URL SHORTNER

    Args:
        object ([type]): Url shortner extends from object
    """

    def __init__(self, url: str,api_key:str):
        self.url: str = url
        self.bitly = bitly_api.Connection(access_token=api_key)

    def get_url(self):
        return self.url

    def short_url(self):
        return self.bitly.shorten(self.url)["url"]
