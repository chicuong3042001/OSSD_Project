import requests
import re
from bs4 import BeautifulSoup

from apps.home.utils import FacebookInitData, Utils, ErrorCode


class GetFacebookInitData:
    def __init__(self, facebook):
        self.facebook = facebook

    def task(self):
        url = 'https://www.facebook.com'
        headers = {'cookie': self.facebook.cookie, 'User-Agent': self.facebook.user_agent}
        response = requests.get(url, headers=headers)
        data = response.text

        fbdtsg = Utils.cut_string_start_end(data, 'fb_dtsg" value="', '"')
        if not fbdtsg:
            fbdtsg = Utils.cut_string_start_end(data, 'DTSGInitialData",[],{"token":"', '"')

        revision = Utils.cut_string_start_end(data, 'client_revision":', ',')
        jazoest = Utils.cut_string_start_end(data, '&jazoest=', '"')
        facebookInitData = FacebookInitData()
        facebookInitData.fbdtsg = fbdtsg
        facebookInitData.revision = revision
        facebookInitData.jazoest = jazoest
        return facebookInitData