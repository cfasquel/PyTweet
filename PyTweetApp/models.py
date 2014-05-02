#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
	author = models.ForeignKey(User)
	mentions = models.ManyToManyField(Mention, through='TweetMention')
	hashtags = models.ManyToManyField(Hashtag, through='TweetHashtag')
	text = models.TextField(max_length=140)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

class Mention(models.Model):
	mentionned_user = models.ForeignKey(User)

class TweetMention(models.Model):
	tweet = models.ForeignKey(Tweet)
	mention = models.ForeignKey(Mention)

class Hashtag(models.Model):
	name = models.TextField(max_length=40)

class TweetHashtag(models.Model):
	tweet = models.ForeignKey(Tweet)
	hashtag = models.ForeignKey(Hashtag)

def __unicode__(self):
		return self.text