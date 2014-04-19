#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	text = """<h1>Bienvenue sur PyTweet !</h1><p>Voici la première vue de l'application.</p>"""
  	return HttpResponse(text)