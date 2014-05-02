from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('PyTweetApp.views',
	url(r'^admin', include(admin.site.urls)),
	url(r'^Hashtag$', 'hashtag'),
	url(r'^SignUp$', 'signup'),
	url(r'^LogOut$', 'logout'),
	url(r'^TweetLine$', 'tweetline'),
	url(r'^(?P<username>.+)$', 'profil'),
	url(r'^$', 'home', name="home"),
)