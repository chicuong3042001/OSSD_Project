from urllib.parse import quote
from apps.home.utils import Utils
import requests
class ScanYoutubeChannel:

    def __init__(self, keyword):
        self.keyword = quote(keyword)

    def scan(self):
        list_channel_id = []
        apiSearchByKeyword = f'https://www.googleapis.com/youtube/v3/search?key={Utils.YTB_API_KEY()}&part=snippet&type=channel&q={self.keyword}&maxResults=50'
        response = requests.get(apiSearchByKeyword)
        result = response.json()
        if "items" in result:
            list_channel_id = [item["id"]["channelId"] for item in result["items"]]

        api_scan_youtube_channel = f"https://www.googleapis.com/youtube/v3/channels?part=brandingSettings,snippet,contentDetails,statistics&id={','.join(list_channel_id)}&key={Utils.YTB_API_KEY()}"
        response = requests.get(api_scan_youtube_channel)
        result = response.json()

        if "items" in result or result.get("kind") == "youtube#channelListResponse":
            return result

        raise Exception("Xảy ra lỗi khi quét kênh Youtube")