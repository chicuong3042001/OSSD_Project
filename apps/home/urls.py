# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('youtube-searching', views.youtube_searching, name='youtube-searching'),
    path('scan-youtube-channel', views.scanYoutubeChannel, name='scan-youtube-channel'),
    path('favorite-channel', views.favoriteChannel, name='favorite-channel'),
    path('discover-youtube', views.discoverYoutube, name='discover-youtube'),
    path('download-youtube/', views.download_video, name='download_video'),
    path('videos/<str:filename>/', views.serve_video, name='serve_video'),
    path('facebook-searching', views.facebook_searching, name='facebook-searching'),
    path('scan-fanpage-info', views.scanFanpageInfo, name='scan-fanpage-info'),
    path('favorite-fanpage', views.favoriteFanpage, name='favorite-fanpage'),
    path('bookmark', views.bookmark, name='bookmark'),
    path('get-list-bookmark-fanpage', views.getListBookmarkFanpage, name='get-list-bookmark-fanpage'),
    path('get-list-bookmark-youtube-channel', views.getListBookmarkYoutubeChannel, name='get-list-bookmark-youtube-channel'),
    path('unfavorite-channel', views.unfavoriteChannel, name='unfavorite-channel'),
    path('unfavorite-fanpage', views.unfavoriteFanpage, name='unfavorite-fanpage'),
    path('discover-facebook', views.discoverFacebook, name='discover-facebook'),
    path('assets/img/<str:filename>/', views.serve_img, name='serve_img'),
    path('facebook-posting', views.facebook_posting, name='facebook-posting'),
    path('get-facebook-init-data', views.getFacebookInitData, name='get-facebook-init-data'),
    path('upload-video', views.uploadVideo, name='upload-video')

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]
