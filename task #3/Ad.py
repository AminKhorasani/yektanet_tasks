from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser


class Ad(BaseAdvertising):

    def __init__(self, lead_id: int, title: str, img_url: str, link: str, advertiser: Advertiser):

        super().__init__()
        self._id = lead_id
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def link(self) -> str:
        return self._link

    @link.setter
    def link(self, new_link):
        self._link = new_link

    @property
    def img_url(self) -> str:
        return self._img_url

    @img_url.setter
    def img_url(self, new_img_url):
        self._img_url = new_img_url

    @property
    def advertiser(self) -> Advertiser:
        return self._advertiser

    @advertiser.setter
    def advertiser(self, new_advertiser: Advertiser):
        self._advertiser = new_advertiser

    def inc_clicks(self):
        self.clicks += 1
        self._advertiser.inc_clicks()

    def describe_me(self):
        print("Ad information")
