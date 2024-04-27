from urllib.parse import quote

import requests

from apps.home.request import GetFacebookInitData
from apps.home.utils import Utils


class ScanFanpageInfo:
    def __init__(self, facebook, keyword):
        self.facebook = facebook
        self.keyword = quote(keyword)
        self.facebookInitData = None

        
    def scan(self):
        url = f"https://graph.facebook.com/?method=post&batch=%5B%7B%20%22method%22%3A%22GET%22%2C%22name%22%3A%22search-pages%22%2C%20%22relative_url%22%3A%22pages/search%3Fq%3D{self.keyword}%26limit%3D80%22%2C%20%22omit_response_on_success%22%3Afalse%2C%7D%2C%20%7B%20%22method%22%3A%22GET%22%2C%20%22relative_url%22%3A%22%3Fids%3D%7Bresult%3Dsearch-pages%3A%24.data.*.id%7D%22%7D%5D&access_token=EAABwzLixnjYBO6UvTJ4NdnFEKV105VJlW5BdKjpYOXZAAiztXiEhCCmeAYaJtwJVZBotqPqttEoPJU9HQw6OIpPpQmgDK9gHf6z2LXWsRHbZBUfxi5V5pDOQbPGjZCDD4RbCRugDj6ZAjdytkT3VncF97aghmYODn7i2b4Kfr6jsrY8TZBODiMMFOQY8lUmhlzTB4ZD&include_headers=false"
        response = requests.get(url)
        return response.text
