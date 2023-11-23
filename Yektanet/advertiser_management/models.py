from django.db import models


class Advertiser(models.Model):

    # fields
    name = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)


class Ad(models.Model):

    # fields
    title = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    img_url = models.URLField(max_length=300)
    landing = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.PROTECT, null=True)
