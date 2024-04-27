import urllib.parse

import requests

from apps.home.request import GetFacebookInitData
from apps.home.utils import Utils


class UploadAttachment:
    upload_params = {
        'lsd': urllib.parse.quote(Utils.make_id(22)),
        'spin_t': Utils.getSpinT(),
        '__s': f"{Utils.make_id(6)}:{Utils.make_id(6)}:{Utils.make_id(6)}",
        'waterfall_id': urllib.parse.quote(Utils.make_id(32)),
        'upload_id': Utils.make_id(32),
        'session_id': urllib.parse.quote(Utils.make_id(16)),
        '__hsi': "7" + Utils.make_number(18),
        '__usid': f"6-{Utils.make_id(13)}:{Utils.make_id(16)}:0-{Utils.make_id(13)}-RV=6:F=",
        '__hs': urllib.parse.quote("19568.BP:bizweb_pkg.2.0..0")
    }

    def __init__(self, facebook, fanpage):
        self.facebook = facebook
        self.fanpage = fanpage
        self.facebookInitData = None

    def startUpload(self, fileInfo):
        get_facebook_init = GetFacebookInitData(facebook=self.facebook)
        if self.facebookInitData is None:
            self.facebookInitData = get_facebook_init.task()
        url = f"https://vupload-edge-business.facebook.com/ajax/video/upload/requests/start/?av={self.fanpage.fanpage_id}&__a=1"
        waterfall_id = UploadAttachment.upload_params.get('waterfall_id')
        __usid = UploadAttachment.upload_params.get('__usid')
        __s = UploadAttachment.upload_params.get('__s')
        __hsi = UploadAttachment.upload_params.get('__hsi')
        lsd = UploadAttachment.upload_params.get('lsd')
        spin_t = UploadAttachment.upload_params.get('spin_t')
        size = fileInfo.get('size')
        payload = f'file_size={size}&file_extension=mp4&target_id={self.fanpage.fanpage_id}&source=composer&composer_dialog_version=&waterfall_id={waterfall_id}&composer_entry_point_ref=biz_web_content_manager_calendar_view&composer_work_shared_draft_mode=&has_file_been_replaced=false&supports_chunking=true&supports_file_api=true&partition_start_offset=0&partition_end_offset={size}&creator_product=2&spherical=false&video_publisher_action_source=&__usid={__usid}&__user={self.facebook.facebook_id}&%20__a=1&__req=10&__hs=19564.BP%3Abizweb_pkg.2.0..0.0&dpr=2&__ccg=EXCELLENT&__rev={self.facebookInitData.revision}&__s={__s}&__hsi={__hsi}&__dyn={self.facebookInitData.get_dyn()}&__csr=&__comet_req=15&fb_dtsg={urllib.parse.quote(self.facebookInitData.fbdtsg)}&jazoest={self.facebookInitData.jazoest}&lsd={lsd}&__spin_r={self.facebookInitData.revision}&__spin_b=trunk&__spin_t={spin_t}&__jssesw=1'


        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.facebook.cookie,
            'referer': 'https://business.facebook.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': self.facebook.user_agent,
            'x_fb_video_waterfall_id': waterfall_id
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = Utils.parse_json_fb(response.text)
        return data

    def getOffset(self, payload):
        get_facebook_init = GetFacebookInitData(facebook=self.facebook)
        if self.facebookInitData is None:
            self.facebookInitData = get_facebook_init.task()
        lsd = UploadAttachment.upload_params.get('lsd')
        upload_id = UploadAttachment.upload_params.get('upload_id')


        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'authority': 'rupload-sin6-2.up.facebook.com',
            'cookie': self.facebook.cookie,
            'referer': 'https://business.facebook.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': self.facebook.user_agent,
            'x-fb-lsd': lsd
        }
        end_offset = payload.get('end_offset')
        __usid = UploadAttachment.upload_params.get('__usid')
        __s = UploadAttachment.upload_params.get('__s')
        __hsi = UploadAttachment.upload_params.get('__hsi')
        spin_t = UploadAttachment.upload_params.get('spin_t')
        url = f'https://rupload-sin6-2.up.facebook.com/fb_video/{upload_id}-0-{end_offset}?fb_dtsg_ag={urllib.parse.quote(self.facebookInitData.fbdtsg)}&__usid={__usid}&__user={self.facebook.facebook_id}&__a=1&__req=11&__hs=19564.BP%3Abizweb_pkg.2.0..0.0&dpr=2&__ccg=EXCELLENT&__rev={self.facebookInitData.revision}&__s={__s}&__hsi={__hsi}&__dyn={self.facebookInitData.get_dyn()}&__csr=&jazoest={self.facebookInitData.jazoest}&__spin_r={self.facebookInitData.revision}&__spin_b=trunk&__spin_t={spin_t}&__jssesw=1'
        response = requests.request("GET", url, headers=headers)

        return response.text

    def getH(self, fileInfo, payload):
        size = fileInfo.get('size')
        end_offset = payload.get('end_offset')
        video_id = payload.get('video_id')
        composer_session_id = urllib.parse.quote(Utils.make_id(11))
        fileName = urllib.parse.quote(fileInfo.get('fileName'))
        __usid = urllib.parse.quote(UploadAttachment.upload_params.get('__usid'))
        upload_id = UploadAttachment.upload_params.get('upload_id')
        __s = urllib.parse.quote(UploadAttachment.upload_params.get('__s'))
        __hsi = UploadAttachment.upload_params.get('__hsi')
        lsd = UploadAttachment.upload_params.get('lsd')
        spin_t = UploadAttachment.upload_params.get('spin_t')
        get_facebook_init = GetFacebookInitData(facebook=self.facebook)
        if self.facebookInitData is None:
            self.facebookInitData = get_facebook_init.task()

        url = f'https://rupload-sin6-2.up.facebook.com/fb_video/{upload_id}-0-{end_offset}?__usid={__usid}&__user={self.facebook.facebook_id}&%20__a=1&__req=2l&__hs=19566.BP%3Abizweb_pkg.2.0..0.0&dpr=2&__ccg=EXCELLENT&__rev={self.facebookInitData.revision}&__s={__s}&__hsi={__hsi}&__dyn={self.facebookInitData.get_dyn()}&__csr=&fb_dtsg={urllib.parse.quote(self.facebookInitData.fbdtsg)}&jazoest={self.facebookInitData.jazoest}&lsd={lsd}&__spin_r={self.facebookInitData.revision}&__spin_b=trunk&__spin_t={spin_t}&__jssesw=1'

        headers = {
            'authority': 'rupload-sin6-2.up.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'composer_session_id': composer_session_id,
            'Content-Length': str(size),
            'content-type': 'application/json',
            'cookie': self.facebook.cookie,
            'end_offset': str(end_offset),
            'offset': '0',
            'product_media_id': video_id,
            'referer': 'https://business.facebook.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'start_offset': '0',
            'user-agent': self.facebook.user_agent,
            'x-entity-length': str(size),
            'x-entity-name': fileName,
            'x-entity-type': 'application/octet-stream',
            'x-total-asset-size': str(size),
        }

        file_path = "E:\\OSSD_Project\\6910080001769475334.mp4"

        # Đọc nội dung của file video
        with open(file_path, 'rb') as file:
            file_content = file.read()
        payload = file_content

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def receiveUpload(self, fbuploader, payload, fileInfo):
        lsd = UploadAttachment.upload_params.get('lsd')
        waterfall_id = UploadAttachment.upload_params.get('waterfall_id')
        video_id = payload.get('video_id')
        size = fileInfo.get('size')
        __usid = urllib.parse.quote(UploadAttachment.upload_params.get('__usid'))
        session_id = UploadAttachment.upload_params.get('session_id')
        _hs = UploadAttachment.upload_params.get('_hs')
        __s = urllib.parse.quote(UploadAttachment.upload_params.get('__s'))
        __hsi = urllib.parse.quote("7" + Utils.make_number(20))
        spin_t = UploadAttachment.upload_params.get('spin_t')

        headers = {
            'authority': 'vupload-edge-business.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.facebook.cookie,
            'referer': 'https://business.facebook.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': self.facebook.user_agent,
            'x-asbd-id': '129477',
            'x-fb-lsd': lsd,
            'x_fb_video_waterfall_id': waterfall_id
        }

        h = urllib.parse.quote(fbuploader.get('h'))
        data = f"fbuploader_video_file_chunk={h}"

        url = f"https://vupload-edge-business.facebook.com/ajax/video/upload/requests/receive/?av={self.fanpage.fanpage_id}&video_id={video_id}&start_offset=0&end_offset={size}&source=composer&target_id={self.fanpage.fanpage_id}&waterfall_id={waterfall_id}&composer_entry_point_ref=biz_web_content_manager_calendar_view&composer_work_shared_draft_mode=&composer_dialog_version=&has_file_been_replaced=false&supports_chunking=true&upload_speed=&partition_start_offset=0&partition_end_offset={size}&__usid={__usid}&session_id={session_id}&__user={self.facebook.facebook_id}&__a=1&__req=2l&supports_upload_service=true&__csr=&__hs=19568.BP%3Abizweb_pkg.2.0..0.0&dpr=2&__ccg=EXCELLENT&__rev={self.facebookInitData.revision}&__s={__s}&__hsi={__hsi}&__dyn={self.facebookInitData.get_dyn()}&_csr=&fb_dtsg={urllib.parse.quote(self.facebookInitData.fbdtsg)}&jazoest={self.facebookInitData.jazoest}&lsd={lsd}&__spin_r={self.facebookInitData.revision}&__spin_b=trunk&__spin_t={spin_t}&__jssesw=1"
        response = requests.request("POST", url, headers=headers, data=data)

        return response.text

    def uploadPostFanpage(self, description, video_id):
        url = "https://business.facebook.com/api/graphql/"
        lsd = UploadAttachment.upload_params.get('lsd')
        __s = urllib.parse.quote(UploadAttachment.upload_params.get('__s'))
        __hsi = UploadAttachment.upload_params.get('__hsi')
        spin_t = UploadAttachment.upload_params.get('spin_t')
        client_id = Utils.get_logging_interaction_key1()

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.facebook.cookie,
            'dpr': '1.25',
            'referer': f'https://business.facebook.com/latest/home?asset_id={self.fanpage.fanpage_id}',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.facebook.user_agent,
            'viewport-width': '200',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'ComposerStoryCreateMutation',
            'x-fb-lsd': lsd
        }

        payload = f"av={self.fanpage.fanpage_id}&__user={self.facebook.facebook_id}&__a=1&__req=1g&__dyn={self.facebookInitData.get_dyn()}&__csr=&__hs=19568.BP%3Abizweb_pkg.2.0..0.0&dpr=2&__ccg=EXCELLENT&__rev={self.facebookInitData.revision}&__s={__s}&__hsi={__hsi}&__comet_req=15&fb_dtsg={urllib.parse.quote(self.facebookInitData.fbdtsg)}&jazoest={self.facebookInitData.jazoest}&__spin_r={self.facebookInitData.revision}&__spin_b=trunk&__spin_t={spin_t}&lsd={lsd}&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=ComposerStoryCreateMutation&variables=%7B%22input%22%3A%7B%22composer_entry_point%22%3A%22inline_composer%22%2C%22composer_source_surface%22%3A%22newsfeed%22%2C%22composer_type%22%3A%22feed%22%2C%22idempotence_token%22%3A%22{client_id}_FEED%22%2C%22source%22%3A%22WWW%22%2C%22audience%22%3A%7B%22privacy%22%3A%7B%22allow%22%3A%5B%5D%2C%22base_state%22%3A%22EVERYONE%22%2C%22deny%22%3A%5B%5D%2C%22tag_expansion_state%22%3A%22UNSPECIFIED%22%7D%7D%2C%22message%22%3A%7B%22ranges%22%3A%5B%5D%2C%22text%22%3A%22{urllib.parse.quote(description)}%22%7D%2C%22with_tags_ids%22%3A%5B%5D%2C%22inline_activities%22%3A%5B%5D%2C%22explicit_place_id%22%3A%220%22%2C%22text_format_preset_id%22%3A%220%22%2C%22attachments%22%3A%20%5B%7B%22video%22%3A%7B%22id%22%3A%22{video_id}5%22%2C%22notify_when_processed%22%3Atrue%7D%7D%5D%2C%22logging%22%3A%7B%22composer_session_id%22%3A%2225814a7b-4486-4bcc-883c-d7cab509e100%22%7D%2C%22navigation_data%22%3A%7B%22attribution_id_v2%22%3A%22CometHomeRoot.react%2Ccomet.home%2Cvia_cold_start%2C1690252405748%2C774111%2C4748854339%2C%22%7D%2C%22tracking%22%3A%5Bnull%5D%2C%22event_share_metadata%22%3A%7B%22surface%22%3A%22newsfeed%22%7D%2C%22actor_id%22%3A%22{self.fanpage.fanpage_id}%22%2C%22client_mutation_id%22%3A%221%22%7D%2C%22displayCommentsFeedbackContext%22%3Anull%2C%22displayCommentsContextEnableComment%22%3Anull%2C%22displayCommentsContextIsAdPreview%22%3Anull%2C%22displayCommentsContextIsAggregatedShare%22%3Anull%2C%22displayCommentsContextIsStorySet%22%3Anull%2C%22feedLocation%22%3A%22NEWSFEED%22%2C%22feedbackSource%22%3A1%2C%22focusCommentID%22%3Anull%2C%22gridMediaWidth%22%3Anull%2C%22groupID%22%3Anull%2C%22scale%22%3A2%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22homepage_stream%22%2C%22useDefaultActor%22%3Afalse%2C%22inviteShortLinkKey%22%3Anull%2C%22isFeed%22%3Atrue%2C%22isFundraiser%22%3Afalse%2C%22isFunFactPost%22%3Afalse%2C%22isGroup%22%3Afalse%2C%22isEvent%22%3Afalse%2C%22isTimeline%22%3Afalse%2C%22isSocialLearning%22%3Afalse%2C%22isPageNewsFeed%22%3Afalse%2C%22isProfileReviews%22%3Afalse%2C%22isWorkSharedDraft%22%3Afalse%2C%22UFI2CommentsProvider_commentsKey%22%3A%22CometModernHomeFeedQuery%22%2C%22hashtag%22%3Anull%2C%22canUserManageOffers%22%3Afalse%2C%22__relay_internal__pv__IsWorkUserrelayprovider%22%3Afalse%2C%22__relay_internal__pv__IsMergQAPollsrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__StoriesRingrelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=6699738323441020"
        print(payload)
        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text
