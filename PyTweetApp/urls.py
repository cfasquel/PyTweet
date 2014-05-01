from django.conf.urls import patterns, url

urlpatterns = patterns('PyTweetApp.views',
	url(r'^Hashtag$', 'hashtag'),
	url(r'^SignUp$', 'signup'),
	url(r'^LogOut$', 'logout'),
	url(r'^TweetLine$', 'tweetline'),
	url(r'^(?P<username>.+)$', 'profil'),
	url(r'^$', 'home', name="home"),
)