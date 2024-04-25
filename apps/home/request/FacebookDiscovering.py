import requests

from apps.home.request import GetFacebookInitData
from apps.home.utils import Utils
import json

class FacebookDiscovering:
    def __init__(self, facebook, fanpageId):
        self.facebook = facebook
        self.fanpageId = fanpageId
        self.facebookInitData = None

    def task(self, end_cursor=None):
        url = "https://www.facebook.com/api/graphql/"
        get_facebook_init = GetFacebookInitData(facebook=self.facebook)
        if self.facebookInitData is None:
            self.facebookInitData = get_facebook_init.task()
        if end_cursor is not None:
            payload = f'fb_dtsg={self.facebookInitData.fbdtsg}&jazoest={Utils.get_numeric_value(self.facebookInitData.fbdtsg)}&doc_id=6640406622685868&method=post&locale=vi_VN&pretty=false&format=json&purpose=refresh&variables=%7B%22UFI2CommentsProvider_commentsKey%22%3A%22CometSinglePageContentContainerFeedQuery%22%2C%22count%22%3A3%2C%22cursor%22%3A%22{end_cursor}%22%2C%22displayCommentsContextEnableComment%22%3Anull%2C%22displayCommentsContextIsAdPreview%22%3Anull%2C%22displayCommentsContextIsAggregatedShare%22%3Anull%2C%22displayCommentsContextIsStorySet%22%3Anull%2C%22displayCommentsFeedbackContext%22%3Anull%2C%22feedLocation%22%3A%22PAGE_TIMELINE%22%2C%22feedbackSource%22%3A22%2C%22focusCommentID%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22timeline%22%2C%22scale%22%3A2%2C%22useDefaultActor%22%3Afalse%2C%22id%22%3A%22{self.fanpageId}%22%2C%22__relay_internal__pv__IsWorkUserrelayprovider%22%3Afalse%2C%22__relay_internal__pv__IsMergQAPollsrelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesRingrelayprovider%22%3Afalse%7D&fb_api_req_friendly_name=CometModernPageFeedPaginationQuery&fb_api_caller_class=RelayModern&server_timestamps=true'
        else:
            payload = f'fb_dtsg={self.facebookInitData.fbdtsg}&jazoest={Utils.get_numeric_value(self.facebookInitData.fbdtsg)}&doc_id=6640406622685868&method=post&locale=vi_VN&pretty=false&format=json&purpose=refresh&variables=%7B%22UFI2CommentsProvider_commentsKey%22%3A%22CometSinglePageContentContainerFeedQuery%22%2C%22count%22%3A3%2C%22cursor%22%3Anull%2C%22displayCommentsContextEnableComment%22%3Anull%2C%22displayCommentsContextIsAdPreview%22%3Anull%2C%22displayCommentsContextIsAggregatedShare%22%3Anull%2C%22displayCommentsContextIsStorySet%22%3Anull%2C%22displayCommentsFeedbackContext%22%3Anull%2C%22feedLocation%22%3A%22PAGE_TIMELINE%22%2C%22feedbackSource%22%3A22%2C%22focusCommentID%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22timeline%22%2C%22scale%22%3A2%2C%22useDefaultActor%22%3Afalse%2C%22id%22%3A%22{self.fanpageId}%22%2C%22__relay_internal__pv__IsWorkUserrelayprovider%22%3Afalse%2C%22__relay_internal__pv__IsMergQAPollsrelayprovider%22%3Afalse%2C%22__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesRingrelayprovider%22%3Afalse%7D&fb_api_req_friendly_name=CometModernPageFeedPaginationQuery&fb_api_caller_class=RelayModern&server_timestamps=true'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.facebook.cookie
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return parse_json(response.text)

def parse_json(json_string):
    try:
        return json.loads(json_string)
    except Exception:
        return json.loads(json_string.split('\n')[0])