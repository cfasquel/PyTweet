from django.contrib import admin

# Register your models here.

from PyTweetApp.models import Tweet, Hashtag, Member

admin.site.register(Tweet)
admin.site.register(Hashtag)
admin.site.register(Member)
