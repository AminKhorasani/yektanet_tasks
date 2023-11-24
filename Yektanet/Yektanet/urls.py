"""yektanet url configuration

the `urlpatterns` list routes urls to views. for more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
examples:
function views
    1. add an import:  from my_app import views
    2. add an url to urlpatterns:  path('', views.home, name='home')
class-based views
    1. add an import:  from other_app.views import home
    2. add an url to urlpatterns:  path('', home.as_view(), name='home')
including another urlconf
    1. import the include() function: from django.urls import include, path
    2. add an url to urlpatterns:  path('', include('.urls'))
    3. add an url to urlpatterns:  path('advertiser_management', include('advertiser_management.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from advertiser_management import urls

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('advertiser_management.urls')),
]