from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.advertiser_list, name='ads-list'),
    path('click/<slug:pk>', views.ClickAdView.as_view(), name='click-ad-view'),
]
