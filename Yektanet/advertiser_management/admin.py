from django.contrib import admin
from .models import Ad, Advertiser

# register ad and advertiser class in admin
admin.site.register(Ad)
admin.site.register(Advertiser)
