import json


class PostFanpage:
    def __init__(self):
        self._index = None
        self._postId = None
        self._likes = None
        self._comments = None
        self._linkVideo = None
        self._thumbnail = None

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int):
        self._index = value

    @property
    def postId(self) -> str:
        return self._postId

    @postId.setter
    def postId(self, value: str):
        self._postId = value

    @property
    def likes(self) -> int:
        return self._likes

    @likes.setter
    def likes(self, value: int):
        self._likes = value

    @property
    def linkVideo(self) -> str:
        return self._linkVideo

    @linkVideo.setter
    def linkVideo(self, value: str):
        self._linkVideo = value

    @property
    def comments(self) -> int:
        return self._comments

    @comments.setter
    def comments(self, value: int):
        self._comments = value

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail = value