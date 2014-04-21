#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from PyTweetApp.forms import ConnexionForm

# Create your views here.

def home(request):

    if request.method == "POST":
        form = ConnexionForm(request.POST)
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
        form = ConnexionForm()

    return render(request, 'home.html',locals())

def hashtag(request):

	return render(request, 'hashtag.html', locals())

def signup(request):

	return render(request, 'sign-up.html', locals())