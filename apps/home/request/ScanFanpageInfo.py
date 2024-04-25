from urllib.parse import quote

import requests

from apps.home.request import GetFacebookInitData
from apps.home.utils import Utils


class ScanFanpageInfo:
    def __init__(self, facebook, keyword):
        self.facebook = facebook
        self.keyword = quote(keyword)
        self.facebookInitData = None
        self.access_token = 'EAABwzLixnjYBO6UvTJ4NdnFEKV105VJlW5BdKjpYOXZAAiztXiEhCCmeAYaJtwJVZBotqPqttEoPJU9HQw6OIpPpQmgDK9gHf6z2LXWsRHbZBUfxi5V5pDOQbPGjZCDD4RbCRugDj6ZAjdytkT3VncF97aghmYODn7i2b4Kfr6jsrY8TZBODiMMFOQY8lUmhlzTB4ZD'
    def scan(self):
        url = f"https://graph.facebook.com/?method=post&batch=%5B%7B%20%22method%22%3A%22GET%22%2C%22name%22%3A%22search-pages%22%2C%20%22relative_url%22%3A%22pages/search%3Fq%3D{self.keyword}%26limit%3D80%22%2C%20%22omit_response_on_success%22%3Afalse%2C%7D%2C%20%7B%20%22method%22%3A%22GET%22%2C%20%22relative_url%22%3A%22%3Fids%3D%7Bresult%3Dsearch-pages%3A%24.data.*.id%7D%22%7D%5D&access_token={self.access_token}&include_headers=false"
        response = requests.get(url)
        return response.text




    # def scan(self, end_cursor=None):
    #     url = 'https://www.facebook.com/api/graphql/'
    #     get_facebook_init = GetFacebookInitData(facebook=self.facebook)
    #     self.facebookInitData = get_facebook_init.task()
    #     dataPost = {
    #         'av': self.facebook.facebook_id,
    #         '__user': self.facebook.facebook_id,
    #         '__a': '1',
    #         '__req': '8',
    #         '__hs': '19558.HYP:comet_pkg.2.1..2.1',
    #         'dpr': '2',
    #         '__ccg': 'EXCELLENT',
    #         '__rev': self.facebookInitData.revision,
    #         '__s': 'Yv9nmz:R1d4wC:CIvmi6',
    #         '__hsi': '7251283615280292205',
    #         '__dyn': self.facebookInitData.get_dyn(),
    #         '__csr': 'gPthLFiYWcjfIhqqflFO_bi9n4rtPczNdORlkymncRilZRH9OcyCtYZaHBBkBqlaHFdlRJkG8mWp9uvF6J39ejDHCyoPDF2USWG9jAXyHK5kexOqfwAzE9V8kxKqbxWmEOVkeK324898O48O8w8K7U2Mx213x21PxibAwlU6K0kmcwso2Zw9i5AE3-w33U0eLE03Scw2io0vIw4pw3pK06PV8CES04DpE08g81Jo0mJw0zMw1PO0kC0Jk0a7w4lw1x90',
    #         '__comet_req': '15',
    #         'fb_dtsg': self.facebookInitData.fbdtsg,
    #         'jazoest': self.facebookInitData.jazoest,
    #         'lsd': 'olE1lMOtu9FVtZKHZvn0tO',
    #         '__spin_r': self.facebookInitData.revision,
    #         '__spin_b': 'trunk',
    #         '__spin_t': Utils.getSpinT(),
    #         'fb_api_caller_class': 'RelayModern',
    #         'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
    #         'variables': '{"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"8c365fe0-a33b-47a1-9123-39d262f460fe","tsid":null},"experience":{"encoded_server_defined_params":null,"fbid":null,"type":"PAGES_TAB"},"filters":[],"text":"' + self.keyword + '"},"count":5,"cursor":null,"displayCommentsContextEnableComment":false,"displayCommentsContextIsAdPreview":false,"displayCommentsContextIsAggregatedShare":false,"displayCommentsContextIsStorySet":false,"displayCommentsFeedbackContext":null,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":2,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__SearchCometResultsShowUserAvailabilityrelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}',
    #         'server_timestamps': 'true',
    #         'doc_id': '9588053444602381'
    #     }
    #
    #     headers = {
    #         'authority': 'www.facebook.com',
    #         'accept': '*/*',
    #         'accept-language': 'en-US,en;q=0.9',
    #         'content-type': 'application/x-www-form-urlencoded',
    #         'cookie': self.facebook.cookie,
    #         'dpr': '1.25',
    #         'referer': 'https://www.facebook.com/search/pages/?q=tr%E1%BA%A5n%20th%C3%A0nh',
    #         'sec-ch-prefers-color-scheme': 'dark',
    #         'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    #         'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.131", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.131"',
    #         'sec-ch-ua-mobile': '?0',
    #         'sec-ch-ua-model': '""',
    #         'sec-ch-ua-platform': '"Windows"',
    #         'sec-ch-ua-platform-version': '"10.0.0"',
    #         'sec-fetch-dest': 'empty',
    #         'sec-fetch-mode': 'cors',
    #         'sec-fetch-site': 'same-origin',
    #         'user-agent': self.facebook.user_agent,
    #         'viewport-width': '483'
    #     }
    #
    #
    #     response = requests.request("POST", url, headers=headers, data=Utils.build_query_string(dataPost))
    #
    #     return [headers, Utils.build_query_string(dataPost)]