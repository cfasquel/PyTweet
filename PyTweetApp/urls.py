from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('PyTweetApp.views',
	url(r'^admin', include(admin.site.urls)),
	url(r'^SignUp$', 'signup'),
	url(r'^LogOut$', 'logout'),
	url(r'^TweetLine$', 'tweetline'),
	url(r'^Hashtag$', 'hashtaglist'),
	url(r'^Hashtag/(?P<hashtag>.+)$', 'hashtag', name="hashtag"),
	url(r'^Retweet/(?P<idtweet>.+)$', 'retweet', name="retweet"),
	url(r'^Follow/(?P<username>.+)$', 'follow', name="follow"),
	url(r'^Unfollow/(?P<username>.+)$', 'unfollow', name="unfollow"),
	url(r'^(?P<username>.+)/Followers$', 'followerlist', name="followers"),
	url(r'^(?P<username>.+)/Followed$', 'followedlist', name="followed"),
	url(r'^(?P<username>.+)$', 'profil'),
	url(r'^$', 'home', name="home"),
)