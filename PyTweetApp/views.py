#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from PyTweetApp.forms import SignInForm, SignUpForm

# Create your views here.

def home(request):

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return render(request, 'tweet-line.html', locals())
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = SignInForm()

    return render(request, 'home.html',locals())

def hashtag(request):

	return render(request, 'hashtag.html', locals())

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

            newUser.save()

            user = authenticate(username=username, password=password)

            login(request, user)  # nous connectons l'utilisateur

            return render(request, 'tweet-line.html', locals())
    else:
        form = SignUpForm()

    return render(request, 'sign-up.html', locals())

def logout(request):
    auth.logout(request)
    return redirect(home)