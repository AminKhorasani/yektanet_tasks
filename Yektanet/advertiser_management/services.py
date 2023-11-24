from .models import Ad, Advertiser


# finds advertiser by the specified primary key in DB
def get_ads(pk):
    try:
        return Ad.objects.get(pk=pk)
    except Ad.DoesNotExist:
        return None


# finds advertiser by the specified primary key in DB
def get_advertisers(pk):
    try:
        return Advertiser.objects.get(pk=pk)
    except Advertiser.DoesNotExist:
        return None

