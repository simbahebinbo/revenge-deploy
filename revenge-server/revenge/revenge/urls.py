# coding=utf-8

from django.conf.urls import include, url
from django.contrib import admin
from .views import home

urlpatterns = [
    # django admin
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^bomb/', include('bomb.urls', namespace='bomb')),
]
