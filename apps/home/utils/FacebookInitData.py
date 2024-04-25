class FacebookInitData:
    def __init__(self):
        self._fbdtsg = ''
        self._revision = ''

    @property
    def fbdtsg(self):
        return self._fbdtsg

    @fbdtsg.setter
    def fbdtsg(self, value):
        self._fbdtsg = value

    @property
    def revision(self):
        return self._revision

    @revision.setter
    def revision(self, value):
        self._revision = value

    @property
    def jazoest(self):
        return self._jazoest

    @jazoest.setter
    def jazoest(self, value):
        self._jazoest = value

    def get_dyn(self):
        return "1KQdAmm1gxu4U4ifGh28sBBgS5UqxKcwRwAxu3-UcodUbE6u7HzE24xm6Uhx61rxicwcW4o29wmU1a852q3q5U2nwvE6W786q5Esx26UhwWwnElzaw5KzHzoaUae1AwgE5y6E52229wcq1FwKCwyxe"

