# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create_mailing/$', views.create_mailing, name='create_mailing'),
    url(r'^track_open/(?P<mailing_id>\d+)/(?P<subscriber_id>\d+)/$', views.track_open, name='track_open'),
    url(r'^$', views.mailing_list, name='mailing_list'),  # Главная страница
]