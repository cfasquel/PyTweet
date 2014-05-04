#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Hashtag(models.Model):
	name = models.TextField(max_length=100)

	def __unicode__(self):
		return "Hashtag {0}".format(self.name)

class Tweet(models.Model):
	author = models.ForeignKey(User, null=False, related_name='author') # author of the tweet
	mentions = models.ManyToManyField(User, null=True, related_name='mentions') # mentionned people in the tweet
	hashtags = models.ManyToManyField(Hashtag, null=True) # hashtag in the tweet
	text = models.TextField(max_length=140) # the actual text of the tweet
	date = models.DateTimeField(auto_now_add=True, auto_now=False) # creation date of the tweet

	def __unicode__(self):
		return "Tweet de {0}, {1}".format(self.author.username, self.text)

class Member(models.Model): # extention of user model
    user = models.OneToOneField(User) # reference to user model
    retweets = models.ManyToManyField(Tweet, null=True, related_name='retweets') # retweeted tweet list
    followers = models.ManyToManyField(User, null=True, related_name='followers') # followers list
    followed = models.ManyToManyField(User, null=True, related_name='followed') # followed list

    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)