import sys

from apps.home.models import Facebook
from apps.home.utils import Utils
import requests
from bs4 import BeautifulSoup


class GetInfoLogin:
    def __init__(self, cookie, user):
        self.cookie = cookie
        self.user = user

    def getInfoLogin(self):
        facebook = Facebook()
        facebook.cookie = self.cookie.split('|')[0]
        facebook.facebook_id = Utils.cut_string_start_end(self.cookie, 'c_user=', ';')
        facebook.user_agent = self.cookie.split('|')[1]
        url = 'https://web.facebook.com/' + facebook.facebook_id
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        title_text = title_tag.text
        facebook.name = title_text
        facebook.avatar = Utils.graphFB() + facebook.facebook_id + Utils.avatarFBParam()
        facebook.user = self.user
        return facebook
