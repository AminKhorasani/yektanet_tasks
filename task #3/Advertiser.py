from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):

    total_clicks = 0

    def __init__(self, media_id: int, pub_name: str):
        super().__init__()
        self._id = media_id
        self._pubName = pub_name

    @property
    def pub_name(self) -> str:
        return self._pubName

    @pub_name.setter
    def pub_name(self, new_name: str):
        self._pubName = new_name

    def inc_clicks(self):
        self.clicks += 1
        Advertiser.total_clicks += 1

    def describe_me(self) -> None:
        print("Advertiser information")

    @staticmethod
    def get_total_clicks() -> int:
        return Advertiser.total_clicks

    @staticmethod
    def help():
        print("You can create a advertiser with Advertiser class and set the media id and name for that")
        print("If you wanna change the name of an advertiser that created lately, call set_name function")
        print("If you forget the name of an advertiser tht created lately, call get_name function")
        print("if you wanna know total click of an advertiser, call get_total_clicks function")

