#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

	isConnected = True

	if isConnected :
		return render(request, 'tweet-line.html', locals())
  	else :
  		return render(request, 'home.html', locals())