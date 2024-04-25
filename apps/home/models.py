# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Facebook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cookie = models.CharField(max_length=255)
    facebook_id = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255)

class Bookmark(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255, null=True)
    published_at = models.DateTimeField(null=True)
    channel_id = models.CharField(max_length=255, null=True)
    fanpage_id = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.IntegerField(null=True)
    subscribe_count = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=255, null=True)
    banner = models.CharField(max_length=255, null=True)
    playlist_id = models.CharField(max_length=255, null=True)
    checkins = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)


class Fanpage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    fanpage_id = models.CharField(max_length=255)
    fanpage_id_delegate = models.CharField(max_length=255)
    facebook = models.ForeignKey(Facebook, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255)