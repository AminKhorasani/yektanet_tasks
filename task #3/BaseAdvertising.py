class BaseAdvertising:

    def __init__(self):
        self.clicks = 0
        self.views = 0

    def get_clicks(self) -> int:
        return self.clicks

    def get_views(self) -> int:
        return self.views

    def inc_clicks(self) -> None:
        self.clicks += 1

    def inc_views(self) -> None:
        self.views += 1

    def describe_me(self) -> None:
        print("Parent class")
