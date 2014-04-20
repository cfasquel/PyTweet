#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

	isConnected = False

	if isConnected :
		return render(request, 'tweet-line.html', locals())
  	else :
  		return render(request, 'home.html', locals())

def hashtag(request):

	return render(request, 'hashtag.html', locals())

def signup(request):

	return render(request, 'sign-up.html', locals())