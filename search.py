from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib

from requests import request

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

# OAuth credential
CLIENT_ID = 'BlvN6HwRcH8UxKR7Bvn_tA'
CLIENT_SECRET = 'no5m4BEV8ERl1zDxOrJqsbk0KLF6IpiwArsFyswogvvQ175CJa5v9x3TW2Fl1oi1'

# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # + Business ID
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

# search limit
SEARCH_LIMIT = 3


def obtain_bearer_token(host, path):
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def search(bearer_token, lat, long):
    url_params = {
        'lat': lat.replace(' ', '+'),
        'long': long.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }

    return request(API_HOST, SEARCH_PATH, bearer_token ,url_params)