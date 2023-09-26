import everapi
import requests
import json
import requests.exceptions
import logging
import everapi.exceptions


class Client(object):
    api_key = None
    headers = {}
    debug = False
    base = None

    def __init__(self, api_base, api_key=None):

        self.headers['User-Agent'] = 'Everapi_Python'
        self.headers['Accept'] = 'application/json'
        self.headers['Content-Type'] = 'application/json'

        if api_key:
            self.api_key = api_key

        if not api_base:
            raise Exception("No API base defined")

        self.api_base = api_base

        if everapi.debug:
            self.debug = True
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(message)s')

    def _request(self, url, method="GET", params=dict(), data=None,
                 return_type=None):
        url = self.api_base + url

        if self.api_key:
            self.headers['apikey'] = self.api_key

        try:
            if method in ["GET", "DELETE"]:
                response = requests.request(
                    method, url, headers=self.headers, params=params)

            elif method == "POST":
                if self.debug:
                    logging.debug(data)
                response = requests.request(
                    method, url, headers=self.headers, params=params, json=data)

            else:
                raise Exception("Method not supported")

            if response.status_code == 429:
                if 'x-ratelimit-remaining-quota-month' in response.headers:
                    quota = response.headers['x-ratelimit-remaining-quota-month']
                    if int(quota) <= 0:
                        raise everapi.exceptions.QuotaExceeded()
                    raise everapi.exceptions.RateLimitExceeded()

            elif response.status_code == 403:
                raise everapi.exceptions.NotAllowed()

            elif response.status_code == 401:
                raise everapi.exceptions.IncorrectApikey()

            response_obj = json.loads(response.text)

            if self.debug:
                logging.debug(response_obj)

            if "errors" in response_obj:
                raise everapi.exceptions.ApiError(
                    "API returned errors:", response_obj['errors'])

            return response_obj

        except requests.exceptions.RequestException:
            raise
