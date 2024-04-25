import requests

from .GetFacebookInitData import GetFacebookInitData
from apps.home.utils import Utils, ErrorCode


class FanpageScanning:
    def __init__(self, facebook):
        self.facebook = facebook
        self.facebookInitData = None

    def task(self, end_cursor=None):
        get_facebook_init = GetFacebookInitData(facebook=self.facebook)
        self.facebookInitData = get_facebook_init.task()
        url = 'https://business.facebook.com/api/graphql/'
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://business.facebook.com',
            'referer': 'https://business.facebook.com/',
            'sec-ch-ua': '"Chromium";v="91", " Not;A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-site': 'same-origin',
            'iewport-width': '874',
            'x-fb-friendly-name': 'MediaUploadFBDefaultServerConfigurationRetrieverQuery',
            'cookie': self.facebook.cookie,
            'user_agent': self.facebook.user_agent
        }

        params = self.build_param(end_cursor)
        response = requests.post(url, data=params, headers=headers)
        return response.json()

    def build_param(self, end_cursor=None):
        usid = '6-' + Utils.make_id(13) + ':' + Utils.make_id(13) + ':0-' + Utils.make_id(13) + '-RV=6:F='
        params = {
            'av': self.facebook.facebook_id,
            '__user': self.facebook.facebook_id,
            '__usid=': usid,
            '__a': '1',
            '__dyn': self.facebookInitData.get_dyn(),
            '__csr': '',
            '__req': '3h',
            '__hs': '19259.BP:media_manager_pkg.2.0.0.0.0',
            'dpr': '2',
            '__ccg': 'EXCELLENT',
            '__rev': self.facebookInitData.revision,
            '__s': Utils.make_id(6) + ':' + Utils.make_id(6) + ':' + Utils.make_id(6),
            '__hsi': '7' + Utils.make_number(20),
            '__comet_req': '0',
            'fb_dtsg': self.facebookInitData.fbdtsg,
            'jazoest': Utils.get_numeric_value(self.facebookInitData.fbdtsg),
            'lsd': Utils.make_id(22),
            '__jssesw': '1',
            'fb_api_caller_class': 'RelayModern'
        }

        if end_cursor:
            params['fb_api_req_friendly_name'] = 'MediaManangerPagePickerPageListPaginationQuery'
            params['variables'] = '{"count":5,"cursor":"' + end_cursor + '","permissionFilter":"NULL","searchQuery":""}'
            params['doc_id'] = '4990400654385683'
        else:
            params['fb_api_req_friendly_name'] = 'MediaManangerPagePickerPageListContainerQuery'
            params['variables'] = '{"permissionFilter":"NULL","searchQuery":"","count":6,"cursor":null}'
            params['doc_id'] = '4885710031544414'

        params['server_timestamps'] = 'true'
        return params



