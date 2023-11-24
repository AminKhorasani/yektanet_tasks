from django.db import models


class Advertiser(models.Model):

    # fields
    name = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def inc_clicks(self):
        self.clicks += 1
        self.save()

    def inc_views(self):
        self.views += 1
        self.save()


class Ad(models.Model):

    # fields
    title = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    img_url = models.URLField(max_length=1000)
    link = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads', null=True)

    def __str__(self):
        return self.title

    def inc_clicks(self):
        self.clicks += 1
        self.advertiser.inc_clicks()
        self.save()

    def inc_views(self):
        self.views += 1
        self.advertiser.inc_views()
        self.save()
