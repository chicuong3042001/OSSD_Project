import json

import requests

from apps.home.utils import Utils


class YoutubeDiscovering:
    def __init__(self, playlistId):
        self.playlistId = playlistId

    def getListVideo(self):
        listVideoId = []
        apiGetListVideoId = f"https://www.googleapis.com/youtube/v3/playlistItems?playlistId={self.playlistId}&key={Utils.YTB_API_KEY()}&part=snippet,id&maxResults=50"
        response = requests.get(apiGetListVideoId)
        result = response.json()
        # Lấy ra các video id
        if 'items' in result:
            listVideoId = [item['snippet']['resourceId']['videoId'] for item in result['items']]

        # Lấy dữ liệu video bằng danh sách ID
        urlGetInfoVideoYoutubeByListId = f"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&id={','.join(listVideoId)}&key={Utils.YTB_API_KEY()}"
        resultInfoVideoYoutubeOfListId = requests.get(urlGetInfoVideoYoutubeByListId)
        listVideoYoutube = resultInfoVideoYoutubeOfListId.json().get('items')

        return listVideoYoutube