# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
import os
from urllib.parse import unquote

import requests
from django import template
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from .models import Fanpage, Facebook, Bookmark
from django.contrib.auth.models import User
from apps.home.request import GetInfoLogin, FanpageScanning, ScanYoutubeChannel, YoutubeDiscovering, ScanFanpageInfo, \
    FacebookDiscovering, GetFacebookInitData, UploadAttachment
from pytube import YouTube

from .utils import PostFanpage


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def dashboard(request):
    context = {'facebook': None, 'list_fanpage': None}
    user = User.objects.get(id=request.user.id)
    try:
        facebook = Facebook.objects.get(id=user.facebook.id)
        context['facebook'] = facebook
    except Exception:
        pass
    try:
        list_fanpage = Fanpage.objects.filter(facebook_id=facebook.id)
        context['list_fanpage'] = list_fanpage
    except Exception:
        pass

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'get_info_login':
            cookie = request.POST.get('facebook_cookie')
            get_info = GetInfoLogin(cookie=cookie, user=user)
            facebook = get_info.getInfoLogin()
            facebook.save()
            user.facebook = facebook
            user.save()
            context['facebook'] = facebook
            return redirect('dashboard')

        if form_type == 'fanpage_scanning':
            fanpageScanning = FanpageScanning(facebook=facebook)
            data = fanpageScanning.task()
            edges = data["data"]["media_manager_user"]["all_pages_passed_permission_filter"]["edges"]
            for edge in edges:
                node = edge["node"]
                fanpage = Fanpage()
                fanpage.fanpage_id = node["id"]
                fanpage.name = node["name"]
                fanpage.avatar = node["profile_pic_uri"]
                fanpage.facebook = facebook
                fanpage.save()
            return redirect('dashboard')
    return render(request, 'app/dashboard.html', context)


@login_required(login_url="/login/")
def youtube_searching(request):
    return render(request, 'app/youtube-searching.html')

@login_required(login_url="/login/")
def scanYoutubeChannel(request):
    keyword = request.GET.get('keyword')
    scanner = ScanYoutubeChannel(keyword)
    result = scanner.scan()
    return JsonResponse(result)

@login_required(login_url="/login/")
def favoriteChannel(request):
    data = json.loads(json.loads(request.body))
    try:
        bookmark = Bookmark.objects.get(name=data['_name'])
    except Bookmark.DoesNotExist:
        bookmark = Bookmark(
            name=data['_name'],
            platform='Youtube',
            published_at=data['_publishedAt'],
            channel_id=data['_channelId'],
            user_id=request.user.id,
            view_count=data['_viewCount'],
            subscribe_count=data['_subscriberCount'],
            thumbnail=data['_thumbnail'],
            banner=data['_banner'],
            playlist_id=data['_playlistId']
        )
    bookmark.view_count = data['_viewCount']
    bookmark.subscribe_count = data['_subscriberCount']
    bookmark.thumbnail = data['_thumbnail']
    bookmark.banner = data['_banner']
    bookmark.save()

    return HttpResponse(f"Yêu thích kênh {bookmark.name} thành công")

@login_required(login_url="/login/")
def discoverYoutube(request):
    global youtube_channel
    if 'channel' in request.GET:
        youtube_channel = request.GET['channel']

    data = json.loads(youtube_channel)
    playlistId = data.get('_playlistId')
    youtubeDiscovering = YoutubeDiscovering(playlistId)
    listVideo = youtubeDiscovering.getListVideo()
    context = {
        'listVideo': listVideo,
        'name': data.get('_name'),
        'subscriberCount': data.get('_subscriberCount'),
        'viewsCount': data.get('_viewCount'),
        'thumbnail': data.get('_thumbnail'),
        'banner': data.get('_banner')
    }

    return render(request, 'app/discover-youtube.html', context)

@login_required(login_url="/login/")
def download_video(request):
    if request.method == 'POST' and request.is_ajax():
        link = request.POST.get('url')

        try:
            yt = YouTube(link)
            title = yt.title
        except:
            print("Connection Error")

        mp4_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        # Chọn stream đầu tiên trong danh sách, có chất lượng cao nhất
        d_video = mp4_streams.first()

        try:
            output_path = os.path.join(settings.MEDIA_ROOT, 'videos')
            d_video.download(output_path)
            video_url = settings.MEDIA_URL + 'videos/' + d_video.default_filename
            return JsonResponse({'success': True, 'video_url': video_url, 'video_title': title})
        except:
            print("Some Error!")

    return JsonResponse({'success': False})

@login_required(login_url="/login/")
def serve_video(request, filename):
    video_path = os.path.join(settings.MEDIA_ROOT, 'videos', filename)
    if os.path.exists(video_path):
        with open(video_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
            return response
    else:
        return HttpResponse("File not found", status=404)


@login_required(login_url="/login/")
def facebook_searching(request):
    return render(request, 'app/facebook-searching.html')

@login_required(login_url="/login/")
def scanFanpageInfo(request):
    keyword = request.GET.get('keyword')
    try:
        facebook = Facebook.objects.get(user_id=request.user.id)
    except Exception:
        return HttpResponse("Vui lòng thêm tài khoản Facebook để sử dụng tính năng này.", status=400)

    scanner = ScanFanpageInfo(facebook, keyword)
    result = scanner.scan()
    return HttpResponse(result)

@login_required(login_url="/login/")
def favoriteFanpage(request):
    data = json.loads(json.loads(request.body))
    try:
        bookmark = Bookmark.objects.get(name=data['_fanpageId'])
    except Bookmark.DoesNotExist:
        bookmark = Bookmark(
            name=data['_name'],
            platform='FANPAGE',
            fanpage_id=data['_fanpageId'],
            user_id=request.user.id,
            likes=data['_likes'],
            checkins=data['_checkins'],
            banner=data['_banner']
        )
    bookmark.name = data['_name']
    bookmark.likes = data['_likes']
    bookmark.checkins = data['_checkins']
    bookmark.save()

    return HttpResponse(f"Yêu thích fanpage {bookmark.name} thành công")


@login_required(login_url="/login/")
def bookmark(request):
    return render(request, 'app/bookmark.html')

@login_required(login_url="/login/")
def getListBookmarkFanpage(request):
    try:
        bookmark = serializers.serialize('json', Bookmark.objects.filter(platform='FANPAGE', user_id=request.user.id))
    except Bookmark.DoesNotExist:
        bookmark = serializers.serialize('json', [])

    return HttpResponse(bookmark)

@login_required(login_url="/login/")
def getListBookmarkYoutubeChannel(request):
    try:
        bookmark = serializers.serialize('json', Bookmark.objects.filter(platform='Youtube', user_id=request.user.id))
    except Bookmark.DoesNotExist:
        bookmark = serializers.serialize('json', [])

    return HttpResponse(bookmark)

@login_required(login_url="/login/")
def unfavoriteChannel(request):
    data = json.loads(json.loads(request.body))
    bookmark = Bookmark.objects.get(name=data['_name'])
    bookmark.delete()
    return HttpResponse(f"Bỏ yêu thích kênh {bookmark.name} thành công")

@login_required(login_url="/login/")
def unfavoriteFanpage(request):
    data = json.loads(json.loads(request.body))
    bookmark = Bookmark.objects.get(fanpage_id=data['_fanpageId'])
    bookmark.delete()
    return HttpResponse(f"Bỏ yêu thích fanpage {bookmark.name} thành công")

@login_required(login_url="/login/")
def discoverFacebook(request):
    global fanpage
    if 'fanpage' in request.GET:
        fanpage = request.GET['fanpage']

    facebook = Facebook.objects.get(user=request.user.id)
    data = json.loads(fanpage)
    facebookDiscovering = FacebookDiscovering(facebook, data.get('_fanpageId'))
    end_cursor = None
    listPost = list()
    while True:
        dataRequest = facebookDiscovering.task(end_cursor)
        # return JsonResponse(dataRequest)
        listPostInfo = dataRequest['data']['node']['timeline_feed_units']['edges']
        for post in listPostInfo:
            postFanpage = get_post_fanpage(post)
            if postFanpage:
                listPost.append(postFanpage)

        has_next_page = dataRequest['data']['node']['timeline_feed_units']['page_info']['has_next_page']
        if not has_next_page:
            break
        else:
            end_cursor = dataRequest['data']['node']['timeline_feed_units']['page_info']['end_cursor']

    fanpageData = {
        'avatar': data.get('_avatar'),
        'name': data.get('_name'),
        'banner': data.get('_banner'),
        'likes': data.get('_likes'),
        'checkins': data.get('_checkins')
    }

    context = {
        'listPost': json.dumps([post.__dict__ for post in listPost]),
        'fanpage': fanpageData,
    }

    return render(request, 'app/discover-facebook.html', context)

@login_required(login_url="/login/")
def get_post_fanpage(data_post):
    post_fanpage = PostFanpage()

    node = data_post.get('node', {})
    comet_sections = node.get('comet_sections', {})
    content = comet_sections.get('content', {})
    story = content.get('story', {})
    feedback = comet_sections.get('feedback', {})
    story_feedback_context = feedback.get('story', {}).get('feedback_context', {})
    ufi_renderer = story_feedback_context.get('feedback_target_with_context', {}).get('ufi_renderer', {})
    try:
        attachment = story.get('attachments', [{}])[0]
    except Exception:
        return None
    styles = attachment.get('styles', {})

    post_fanpage.postId = node.get('post_id')

    post_fanpage.likes = ufi_renderer.get('feedback', {}).get('comet_ufi_summary_and_actions_renderer', {}).get(
        'feedback', {}).get('reaction_count', {}).get('count')
    post_fanpage.comments = ufi_renderer.get('feedback', {}).get('total_comment_count')

    typename = styles.get('__typename')
    if typename and 'Video' in typename:
        post_fanpage.typename = 'Video'
        uri = styles.get('attachment', {}).get('media', {}).get('image', {}).get('uri')
        if uri:
            post_fanpage.thumbnail = uri
        playableUrlHd = styles.get('attachment', {}).get('media', {}).get('browser_native_hd_url')
        playableUrl = styles.get('attachment', {}).get('media', {}).get('browser_native_sd_url')
        post_fanpage.linkVideo = playableUrlHd if playableUrlHd else playableUrl
        return post_fanpage

    return None

@login_required(login_url="/login/")
def serve_img(request, filename):
    video_path = os.path.join(settings.MEDIA_ROOT, 'apps', 'static', 'assets', 'img', filename)
    if os.path.exists(video_path):
        with open(video_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            return response
    else:
        return HttpResponse("File not found", status=404)


from django.core.serializers import serialize


@login_required(login_url="/login/")
def facebook_posting(request):
    context = {'facebook': None, 'list_fanpage': None}
    user = User.objects.get(id=request.user.id)
    try:
        facebook = Facebook.objects.get(id=user.facebook.id)
        context['facebook'] = serialize('json', [facebook])
    except Exception:
        pass
    try:
        list_fanpage = Fanpage.objects.filter(facebook_id=facebook.id)
        context['list_fanpage'] = serialize('json', list_fanpage)
    except Exception:
        pass

    return render(request, 'app/facebook-posting.html', context)

@login_required(login_url="/login/")
def getFacebookInitData(request):
    user = User.objects.get(id=request.user.id)
    facebook = Facebook.objects.get(id=user.facebook.id)
    getFacebookInitData = GetFacebookInitData(facebook)
    facebookInitData = getFacebookInitData.task()
    data_dict = {
        "fbdtsg": facebookInitData.fbdtsg,
        "revision": facebookInitData.revision,
        "jazoest": facebookInitData.jazoest
    }

    return JsonResponse(data_dict)

@login_required(login_url="/login/")
def uploadVideo(request):
    postUpload = json.loads(request.POST.get('postUpload'))
    fanpageData = postUpload.get('fanpage')
    user = User.objects.get(id=request.user.id)
    facebook = Facebook.objects.get(id=user.facebook.id)
    fileInfo = postUpload.get('fileInfo')
    fanpage = Fanpage.objects.get(fanpage_id=fanpageData.get('fanpageId'))
    uploadAttachment = UploadAttachment(facebook=facebook, fanpage=fanpage)
    data = uploadAttachment.startUpload(fileInfo)
    payload = data.get('payload')
    offset = uploadAttachment.getOffset(payload)
    fbuploader = uploadAttachment.getH(fileInfo, payload)
    uploadAttachment.receiveUpload(fbuploader, payload, fileInfo)
    dataPost = uploadAttachment.uploadPostFanpage(postUpload.get('discription'), payload.get('video_id'))
    return HttpResponse(dataPost)