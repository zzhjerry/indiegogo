import json
import inspect
import requests
from . import models

class Client(object):

    """python client for indiegogo"""

    def __init__(self):
        self.api_key = None
        self.base_url = 'https://api.indiegogo.com/1.1/'
        self.caller_status = {}

    def search_campaigns(self, **kwargs):
        url = 'search/campaigns.json'
        return self.page(url, 'Campaign', **kwargs)

    def call_server(self, url, **params):
        params['api_token'] = self.api_key
        r = requests.get('{}{}'.format(self.base_url, url), params=params)
        if not r.status_code == 200: return None
        return r.text

    def page(self, url, cls, **kwargs):
        caller = inspect.stack()[1][3]
        if kwargs.get('page', None) is None:
            if caller in self.caller_status:
                next_page = self.caller_status[caller]['next']
                kwargs['page'] = next_page
                if not next_page:
                    return None

        json_string = self.call_server(url, **kwargs)
        json_obj = json.loads(json_string)
        page = Page()
        for key, value in json_obj.items():
            setattr(page, key, value)
        page.response = models.parse_list(page.response, cls)

        self.caller_status[caller] = page.pagination

        return page


class Page(object):


    def __init__(self):
        self.response = None
        self.count = None
        self.pagination = None

    def __getitem__(self, index):
        return self.response[index]
