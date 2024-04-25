from apps.home.request import GetFacebookInitData


class HandlePost:
    def __init__(self, facebook, fanpage):
        self.facebook = facebook
        self.fanpage = fanpage
        self.facebookInitData = None
        get_facebook_init = GetFacebookInitData(facebook=self.facebook)
        self.facebookInitData = get_facebook_init.task()

    def startUpload(self):
        pass