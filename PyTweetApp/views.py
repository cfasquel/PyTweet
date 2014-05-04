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
			username = form.cleaned_data["username"]  # retreiving user name
			password = form.cleaned_data["password"]  # ...and password
			user = authenticate(username=username, password=password)

			if user :  # if authentication worked
				login(request, user)  # user connection
				return redirect(tweetline) # redirecting to tweet-line
			else :
				error = True

	else :
		if request.user.is_authenticated() :
			return redirect(tweetline)
		else :
			form = SignInForm()

	return render(request, 'home.html',locals())




def tweetline(request):
	
	if request.method == "POST" : # User is sending a new tweet

		form = NewTweetForm(request.POST)

		if form.is_valid() :

			tweet_message = form.cleaned_data["tweet_message"]

			tweet = Tweet(text=tweet_message, author=request.user)

			tweet.save()

			# checking if there is mentions or hashtags

			tweet_message_splited = tweet_message.split(' ')

			for tweet_word in tweet_message_splited :

				if tweet_word[0] == '@' : # There is a mention
					try :
						mentionned_user = User.objects.get(username=tweet_word[1:])
						tweet.mentions.add(mentionned_user)
					except User.DoesNotExist :
						continue
				elif tweet_word[0] == '#' : # There is a hashtag
						hashtag = Hashtag.objects.get_or_create(name=tweet_word[1:])
						tweet.hashtags.add(hashtag[0])

			tweet.save()
			form = NewTweetForm()

		else :

			error = True

	else :

		form = NewTweetForm()

	user_profil = User.objects.get(username=request.user.username)

	tweets = Tweet.objects.filter(Q(mentions=request.user) | # if user is mentionned
								  Q(author=user_profil) | # if user is the author
								  #Q(id__in=request.user.retweets.all()) # if this is a retweet (didn't managed to make it work, targetting id)
								  Q(author__in=request.user.member.followed.all())).order_by('-date') # if user is followed by logged in user

	return render(request, 'tweet-line.html', locals())




def profil(request, username):

	user_profil = User.objects.get(username=username)

	tweets = Tweet.objects.filter(author=user_profil).order_by('-date')

	followers = user_profil.member.followers.count()
	followed = user_profil.member.followed.count()

	nbrtweets = Tweet.objects.filter(author=user_profil).count()

	return render(request, 'profil.html', locals())

def followerlist(request, username):

	user_profil = User.objects.get(username=username)
	followers = user_profil.member.followers.all()

	return render(request, 'follower-list.html', locals())

def followedlist(request, username):

	user_profil = User.objects.get(username=username)
	followed = user_profil.member.followed.all()

	return render(request, 'followed-list.html', locals())

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
	user_to_follow.member.followers.add(request.user)
	user_to_follow.member.save()
	request.user.member.followed.add(user_to_follow)
	request.user.member.save()

	return redirect(tweetline)

def unfollow(request, username):

	user_to_unfollow = User.objects.get(username=username)
	user_to_unfollow.member.followers.remove(request.user)
	user_to_unfollow.member.save()
	request.user.member.followed.remove(user_to_unfollow)
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
			newUser.first_name = firstname
			newUser.last_name = lastname

			newUser.save()
			
			member = Member(user=newUser)

			member.save()

			newUser = authenticate(username=username, password=password)

			login(request, newUser)  # user connection on sign up

			return redirect(tweetline)

	else:

		form = SignUpForm()

	return render(request, 'sign-up.html', locals())

def logout(request):

	auth.logout(request)
	return redirect(home)