#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
	author = models.ForeignKey(User)
	text = models.TextField(max_length=140)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

def __unicode__(self):
		return self.text