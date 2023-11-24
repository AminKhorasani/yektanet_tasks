from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ad, Advertiser
from django.views.generic import RedirectView
from .services import get_advertisers, get_ads
from django.contrib import messages


def advertiser_list(request):
    advertisers = Advertiser.objects.all()  # Queryset of all advertisers in DB
    for advertiser in advertisers:
        ads_list = advertiser.ads.all()     # Queryset of all ads in one advertiser
        for ad in ads_list:
            ad.inc_views()

    context = {
        'advertisers': advertisers
    }

    return render(request, 'advertiser_management/ads.html', context=context)


class ClickAdView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad_pk = kwargs['pk']
        ad = get_ads(ad_pk)
        if ad is None:
            messages.error(self.request, 'Could not find any Ad with this specific identifier')
            return reverse('ads-list')
        ad.inc_clicks()
        return redirect('https://www.yektanet.com/')
