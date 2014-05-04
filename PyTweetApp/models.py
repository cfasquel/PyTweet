#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Hashtag(models.Model):
	name = models.TextField(max_length=100)

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

class Member(models.Model):
    user = models.OneToOneField(User)
    retweets = models.ManyToManyField(Tweet, null=True, related_name='retweets')
    followed = models.ManyToManyField(User, null=True, related_name='followed')

    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)