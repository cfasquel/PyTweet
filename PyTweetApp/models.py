#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Hashtag(models.Model):
	name = models.TextField(max_length=40)

	def __unicode__(self):
		return "Hashtag {0}".format(self.name)

class Tweet(models.Model):
	author = models.ForeignKey(User, null=False, related_name='author')
	mentions = models.ManyToManyField(User, null=True, related_name='mentions')
	hashtags = models.ManyToManyField(Hashtag, null=True)
	text = models.TextField(max_length=140)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return "Tweet de {0}, {1}".format(self.author.username, self.text)

# class TweetMention(models.Model):
# 	tweet = models.ForeignKey(Tweet)
# 	mention = models.ForeignKey(Mention)

# class TweetHashtag(models.Model):
# 	tweet = models.ForeignKey(Tweet)
# 	hashtag = models.ForeignKey(Hashtag)