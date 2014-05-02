#-*- coding: utf-8 -*-
from django import forms

class SignInForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SignUpForm(forms.Form):

	firstname = forms.CharField(label="Prénom", max_length=30)
	lastname = forms.CharField(label="Nom", max_length=30)
	email = forms.EmailField(label="E-mail", max_length=50)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)

class NewTweetForm(forms.Form):

	tweet_message = forms.CharField(label="Votre tweet", max_length=140, widget=forms.Textarea)