#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.db.models import Q

from django.core.urlresolvers import reverse

from PyTweetApp.forms import SignInForm, SignUpForm, NewTweetForm

from PyTweetApp.models import Tweet, Hashtag, Member
# Create your views here.

def home(request):

	if request.method == "POST" :

		form = SignInForm(request.POST)

		if form.is_valid() :
			username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
			password = form.cleaned_data["password"]  # … et le mot de passe
			user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes

			if user :  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
				return redirect(tweetline)
			else : #sinon une erreur sera affichée
				error = True

	else :
		if request.user.is_authenticated() :
			return redirect(tweetline)
		else :
			form = SignInForm()

	return render(request, 'home.html',locals())




def tweetline(request):
	
	if request.method == "POST" : # L'utilisateur entre un nouveau tweet

		form = NewTweetForm(request.POST)

		if form.is_valid() :

			tweet_message = form.cleaned_data["tweet_message"]

			tweet = Tweet(text=tweet_message, author=request.user)

			tweet.save()

			# On récupère le tweet et on découvre les mentions à l'interieur

			tweet_message_splited = tweet_message.split(' ')

			for tweet_word in tweet_message_splited :

				if tweet_word[0] == '@' :# L'utilisateur à mentionné quelqu'un
					try :
						mentionned_user = User.objects.get(username=tweet_word[1:])
						tweet.mentions.add(mentionned_user)
					except User.DoesNotExist :
						continue
				elif tweet_word[0] == '#' :
						hashtag = Hashtag.objects.get_or_create(name=tweet_word[1:])
						tweet.hashtags.add(hashtag[0])

			tweet.save()
			form = NewTweetForm()

		else :

			error = True

	else :

		form = NewTweetForm()

	user_profil = User.objects.get(username=request.user.username)
	tweets = Tweet.objects.filter(Q(mentions=user_profil) | Q(author=user_profil) | Q(author__in=request.user.member.followed.all())).order_by('-date')

	return render(request, 'tweet-line.html', locals())




def profil(request, username):

	user_profil = User.objects.get(username=username)

	tweets = Tweet.objects.filter(author=user_profil).order_by('-date')

	return render(request, 'profil.html', locals())



def hashtaglist(request):

	hashtags = Hashtag.objects.all()

	return render(request, 'hashtag-list.html', locals())


def hashtag(request, hashtag):

	hashtag = Hashtag.objects.get(name=hashtag)

	tweets = Tweet.objects.filter(hashtags=hashtag).order_by('-date')

	return render(request, 'hashtag.html', locals())



def retweet(request, idtweet):
	tweet_to_retweet = Tweet.objects.get(id=idtweet)
	request.user.member.retweets.add(tweet_to_retweet)
	request.user.member.save()

	return redirect(tweetline)

def follow(request, username):

	user_to_follow = User.objects.get(username=username)
	request.user.member.followed.add(user_to_follow)
	request.user.member.save()

	return redirect(tweetline)

def unfollow(request, username):

	user_to_follow = User.objects.get(username=username)
	request.user.member.followed.remove(user_to_follow)
	request.user.member.save()

	return redirect(tweetline)

def signup(request):

	if request.method == "POST":
		form = SignUpForm(request.POST)

		if form.is_valid():
			firstname = form.cleaned_data["firstname"]
			lastname = form.cleaned_data["lastname"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			username = form.cleaned_data["username"]

			newUser = User.objects.create_user(username, email, password)
			newUser.first_name, newUser.last_name = firstname, lastname

			member = Member(user=newUser)

			member.save()

			newUser = authenticate(username=username, password=password)

			login(request, newUser)  # nous connectons l'utilisateur

			return redirect(tweetline)

	else:

		form = SignUpForm()

	return render(request, 'sign-up.html', locals())

def logout(request):

	auth.logout(request)
	return redirect(home)